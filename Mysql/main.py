import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine
import glob
from Funciones import *
from Funciones_carga import cargar_datos_en_tabla,carga_incremental
from Funciones_crear import crear_tabla
import warnings
# Suprimir todas las advertenciass
warnings.filterwarnings("ignore")

credenciales = leer_credenciales('credenciales.txt')
usuario = credenciales['usuario']
contrasena = credenciales['contrasena']
host = credenciales['host']
database = credenciales['database']
# Crear la base de datos
crear_base_de_datos(usuario, contrasena)
# Conexión a la base de datos Data_Warehouse
conexion = pymysql.connect(host=host, user=usuario, passwd=contrasena, db=database)
cursor = conexion.cursor()
directorio = 'Datasets'  # Ruta relativa al directorio de trabajo actual
archivos = os.listdir(directorio)
# Conexión para inserción de datos
conexion2 = create_engine(f"mysql+pymysql://{usuario}:{contrasena}@{host}/{database}")
for archivo in archivos:
    if os.path.isfile(os.path.join(directorio, archivo)):
        ruta = os.path.join(directorio, archivo)
        # Procesar el archivo según su tipo
        df = procesar_archivo_por_tipo(ruta, archivo, directorio)
        if df is not None and not df.empty:
            nombre_tabla = obtener_nombre_tabla(ruta)
            # Asegurarse de que el nombre de la tabla es único
            if tabla_existe(cursor, nombre_tabla):
                carga_incremental(cursor, conexion2, nombre_tabla, df)
            else:
                #crear la tabla
                crear_tabla(cursor,nombre_tabla,df)
                # Cargar datos en la tabla
                cargar_datos_en_tabla(conexion2, df, nombre_tabla)

                # Renombrar columnas en la base de datos
                renombrar_columnas_en_tabla(conexion, nombre_tabla, df)
variable_gobal()  
conexion.close()
