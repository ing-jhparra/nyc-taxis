import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine
import glob
from ETL_TaxisBI import EtlTaxisTrip #funcion by camilo 
from ETL import etl_co2_year,etl_co2_transporte,etl_co2021 #funcion by javier
from ETL_noise_pollution import noise_pollution #funcion by Facundo
from ETL_vehiculos import etl_fuel,etl_electrico,etl_hibrido #funcion by Michael

import warnings
# Suprimir todas las advertencias
warnings.filterwarnings("ignore")

# Definir una variable global para controlar la ejecución única
ejecutado3= False
ejecutado2 = False

def obtener_tipo_archivo(ruta):
    _, extension = os.path.splitext(ruta)
    extension = extension.lower()
    if extension == '.xlsx' or extension == '.xls':
        return 'Excel'
    elif extension == '.csv':
        return 'CSV'
    elif extension == '.parquet':
        return 'Parquet'
    else:
        return 'ERROR'
    
def sanitizar_nombre(nombre):
    nombre = str(nombre).lower()   # Convertir a cadena
    nombre = nombre.replace(" ", "_").replace("-", "_")
    nombre = ''.join(e for e in nombre if e.isalnum() or e == '_')
    if nombre[0].isdigit():
        nombre = '_' + nombre
    return nombre[:64] 

def obtener_nombre_tabla(url):
    partes_url = url.split("\\")
    nombre_tabla = partes_url[-1]
    nombre_tabla = nombre_tabla.replace(".csv", "")
    nombre_tabla = nombre_tabla.replace(".xlsx", "")
    nombre_tabla = nombre_tabla.replace(".xls", "")
    nombre_tabla = nombre_tabla.replace(".parquet", "")
    if nombre_tabla == 'my2012-2024-battery-electric-vehicles':
        nombre_tabla = 'electric_vehicles'
    elif nombre_tabla == 'my2012-2024-plug-in-hybrid-electric-vehicles':
        nombre_tabla = 'hybrid_vehicles'
    elif glob.fnmatch.fnmatch(nombre_tabla, 'my*-fuel-consumption-ratings*'):
        nombre_tabla = 'fuel_vehicles'
    return sanitizar_nombre(nombre_tabla)


def tabla_existe(cursor, nombre_tabla):
    nombre_tabla = nombre_tabla.lower()
    cursor.execute("SHOW TABLES")
    nombres_tablas = cursor.fetchall()
    return (nombre_tabla,) in nombres_tablas

def agregar_numero(nombre_tabla):
    partes = nombre_tabla.split('_')
    if partes[-1].isdigit():
        numero = int(partes[-1])
        nuevo_nombre_tabla = '_'.join(partes[:-1]) + '_' + str(numero + 1)
    else:
        nuevo_nombre_tabla = nombre_tabla + '_2'
    return nuevo_nombre_tabla

def identificar_separador_csv(ruta_archivo):
    separadores = {',': 0, ';': 0}  
    with open(ruta_archivo, 'r') as archivo:
        for _ in range(5):  
            linea = archivo.readline()
            for separador in separadores.keys():
                separadores[separador] += linea.count(separador)
    separador_mas_comun = max(separadores, key=separadores.get)
    return separador_mas_comun

def leer_csv_con_codificacion(ruta_archivo, separador):
    try:
        df = pd.read_csv(ruta_archivo, sep=separador, encoding='utf-8')
        return df
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(ruta_archivo, sep=separador, encoding='latin1')
            return df
        except UnicodeDecodeError:
            raise ValueError("No se pudo leer el archivo CSV con las codificaciones 'utf-8' o 'latin1'.")

def crear_base_de_datos(usuario, contrasena):
    conexion = pymysql.connect(host='localhost', user=usuario, passwd=contrasena)
    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Data_Warehouse")
    conexion.close()

def leer_credenciales(ruta):
    credenciales = {}
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            key, value = linea.strip().split('=')
            credenciales[key] = value
    return credenciales

def procesar_archivo_por_tipo(ruta, archivo, directorio):
    tipo_archivo = obtener_tipo_archivo(ruta)
    df = None
    global ejecutado3
    global ejecutado2
    if tipo_archivo == 'Excel':
        df_excel = pd.read_excel(ruta)
        if archivo == 'co2_year.xlsx':
            df = etl_co2_year(df_excel)
        elif archivo == 'transportation.xlsx':
            df = etl_co2_transporte(df_excel)
        elif archivo == 'co2_sector2021.xlsx':
            df = etl_co2021(df_excel)
        else:
            df = df_excel
            # Agregar '_clean' antes de la extensión
            archivo_clean = archivo.replace('.xlsx', '_clean.xlsx')
            # Guardar el DataFrame en un archivo Excel con el nuevo nombre
            file_name = f'Datasets_limpios/{archivo_clean}'
            df.to_excel(file_name, index=False)
    elif tipo_archivo == 'CSV':
        separador = identificar_separador_csv(ruta)
        df_csv = leer_csv_con_codificacion(ruta, separador)
        if archivo == 'annotations.csv':
            df = noise_pollution(df_csv)
        elif archivo == 'my2012-2024-battery-electric-vehicles.csv':
            df = etl_electrico(df_csv)
        elif archivo == 'my2012-2024-plug-in-hybrid-electric-vehicles.csv':
            df = etl_hibrido(df_csv)
        elif glob.fnmatch.fnmatch(archivo, 'my*-fuel-consumption-ratings*.csv'):
            if not ejecutado3:
                df=etl_fuel() # Llamar a la función EtlTaxisTrip para procesar archivos Parquet que cumplen el patrón
                ejecutado3 = True
        else:
            df = df_csv
            # Agregar '_clean' antes de la extensión
            archivo_clean = archivo.replace('.csv', '_clean.csv')
            # Guardar el DataFrame en un archivo Excel con el nuevo nombre
            file_name = f'Datasets_limpios/{archivo_clean}'
            df.to_csv(file_name, index=False)
    elif tipo_archivo == 'Parquet':
        if glob.fnmatch.fnmatch(archivo, 'yellow_tripdata_2023-*.parquet'):
            if not ejecutado2:
                EtlTaxisTrip(directorio, archivo,'Datasets/yellow_tripdata_consolidado.parquet',sample_size=100000) # Llamar a la función EtlTaxisTrip para procesar archivos Parquet que cumplen el patrón
                ejecutado2 = True
        else:
            df = pd.read_parquet(ruta)
    else:
        print('Error: tipo de archivo no soportado')

    return df
def renombrar_columnas_en_tabla(conexion, nombre_tabla, df):
    cursor = conexion.cursor()
    for columna in df.columns:
        tipo_dato = df[columna].dtype
        if tipo_dato == 'int64':
            nuevo_nombre = f"{columna}_int"
        elif tipo_dato == 'float64':
            nuevo_nombre = f"{columna}_float"
        elif tipo_dato == 'object':
            nuevo_nombre = f"{columna}_str"
        elif pd.api.types.is_datetime64_any_dtype(df[columna]):
            nuevo_nombre = f"{columna}_dt"
        else:
            nuevo_nombre = f"{columna}_str"
        query = f"ALTER TABLE {nombre_tabla} CHANGE `{columna}` `{nuevo_nombre}` {tipo_dato_to_sql(tipo_dato)}"
        cursor.execute(query)
    conexion.commit()

def tipo_dato_to_sql(tipo_dato):
    if tipo_dato == 'int64':
        return "INT"
    elif tipo_dato == 'float64':
        return "FLOAT"
    elif tipo_dato == 'object':
        return "VARCHAR(255)"
    elif pd.api.types.is_datetime64_any_dtype(tipo_dato):
        return "DATETIME"
    else:
        return "VARCHAR(255)"

def variable_gobal():
    global ejecutado3
    global ejecutado2
    ejecutado3=False
    ejecutado2=False