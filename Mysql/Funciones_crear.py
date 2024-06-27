import pandas as pd
from sqlalchemy import create_engine
from Funciones import *

import warnings
# Suprimir todas las advertencias
warnings.filterwarnings("ignore")

def obtener_query(nombre_tabla, df):
    query = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (\n"
    for columna in df.columns:
        nombre_columna = sanitizar_nombre(columna)
        tipo_de_dato = df[columna].dtype
        query += f"`{nombre_columna}` "
        if tipo_de_dato == 'int64':
            query += "INT"
        elif tipo_de_dato == 'float64':
            query += "FLOAT"
        elif tipo_de_dato == 'object':
            query += "VARCHAR(255)"
        elif pd.api.types.is_datetime64_any_dtype(df[columna]):
            query += "DATETIME"
        else:
            query += "VARCHAR(255)"
        query += ",\n"
    id_columna = f"id_{nombre_tabla}_int"
    query += f"{id_columna} INT PRIMARY KEY NOT NULL AUTO_INCREMENT\n);"
    return query

def crear_tabla(cursor,nombre_tabla,df):
    query_crear_tabla = obtener_query(nombre_tabla, df)
    cursor.execute(query_crear_tabla)

