import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine, text
from Funciones import *

import warnings
# Suprimir todas las advertencias
warnings.filterwarnings("ignore")



def renombrar_columnas_en_tabla2(conexion, nombre_tabla, df):
    cursor = conexion.cursor()
    for columna in df.columns:
        tipo_dato = df[columna].dtype
        nuevo_nombre = renombrar_columna(columna, tipo_dato)
        query = f"ALTER TABLE {nombre_tabla} CHANGE `{columna}` `{nuevo_nombre}` {tipo_dato_to_sql(tipo_dato)}"
        cursor.execute(query)
    conexion.commit()

# Función para cargar datos en la tabla
def cargar_datos_en_tabla(conexion2, df, nombre_tabla):
    # Sanitizar nombres de columnas del DataFrame
    df.columns = [sanitizar_nombre(col) for col in df.columns]
    # Insertar datos en la tabla
    df.to_sql(nombre_tabla, con=conexion2, if_exists='append', index=False)

def renombrar_columna(col, dtype):
    col = col.lower().replace(' ', '_').replace('-', '_')
    col = ''.join([c if c.isalnum() or c == '_' else '' for c in col])
    return col[:64]

def carga_incremental(cursor, conexion2, nombre_tabla, df):
    # Renombrar columnas en el DataFrame si es necesario
    df.rename(columns={col: renombrar_columna(col, df[col].dtype) for col in df.columns}, inplace=True)

    # Obtener columnas de la tabla en la base de datos
    cursor.execute(f"SHOW COLUMNS FROM {nombre_tabla}")
    columnas_tabla = [col[0].lower() for col in cursor.fetchall()]

    # Filtrar las columnas del DataFrame que existen en la tabla de la base de datos
    columnas_df = [col for col in df.columns if col.lower() in columnas_tabla]

    # Convertir DataFrame a diccionarios para comparación eficiente
    registros_db = {}
    cursor.execute(f"SELECT * FROM {nombre_tabla}")
    for row in cursor.fetchall():
        registros_db[row[0]] = row[1:]

    # Identificar registros nuevos y actualizaciones
    registros_nuevos = []
    registros_actualizar = []
    for index, row in df.iterrows():
        # Acceder a las columnas usando los nombres correctos después del renombrado
        valores = tuple(row[columnas_df].values)
        if valores not in registros_db.values():
            registros_nuevos.append(valores)
        else:
            id_registro = next(key for key, value in registros_db.items() if value == valores)
            registros_actualizar.append((id_registro,) + valores)

    with conexion2.connect() as conn:
        # Insertar registros nuevos
        if registros_nuevos:
            placeholders = ', '.join(['%s'] * len(columnas_df))
            columnas_df_str = ', '.join([f"`{col}`" for col in columnas_df])
            insert_query = text(f"INSERT INTO {nombre_tabla} ({columnas_df_str}) VALUES ({placeholders})")
            for registro in registros_nuevos:
                conn.execute(insert_query, registro)

        # Actualizar registros existentes
        if registros_actualizar:
            set_clause = ', '.join([f"`{col}` = %s" for col in columnas_df])
            update_query = text(f"UPDATE {nombre_tabla} SET {set_clause} WHERE id = %s")
            for registro in registros_actualizar:
                conn.execute(update_query, registro)



