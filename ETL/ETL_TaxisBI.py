import pandas as pd
import pandas as pd
import numpy as np 
import os
import glob

def EtlTaxisTrip(carpeta, archivo_base, archivo_consolidado, sample_size=100000):
    # Cargar informacion de las zonas 
    taxis_zones= pd.read_csv('../Datasets/taxi_zones.csv', sep=';')
    
    # Cargar el DataFrame consolidado si existe
    if os.path.exists(archivo_consolidado):
        df_consolidado = pd.read_parquet(archivo_consolidado)
    else:
        df_consolidado = pd.DataFrame()

    # Obtener todos los archivos que coincidan con el patrón
    all_files = glob.glob(os.path.join(carpeta, archivo_base))
    
    for file in all_files:
        if not os.path.exists(file):
            print(f"Archivo no encontrado: {file}")
            continue
        
        print(f"Procesando archivo: {file}")
        df = pd.read_parquet(file)
        
        # Verificar si el tamaño del muestreo no excede el número de filas del archivo 
        sample_size = min(sample_size, len(df))
        random_indices = np.random.choice(df.index, size=sample_size, replace=False)
        df = df.loc[random_indices]
        
        # Seleccionar columnas a utilizar 
        df = df[['VendorID','tpep_pickup_datetime','tpep_dropoff_datetime','passenger_count','trip_distance','PULocationID','payment_type','fare_amount']]
        
        # Convertir a datetime si no están en ese formato
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        
    # Con la variable 'tpep_pickup_datetime' la usamos para obtener el dia y mes en que se realiza el viaje 
        df['pickup_month'] = df['tpep_pickup_datetime'].dt.month_name()
        df['pickup_day_of_week'] = df['tpep_pickup_datetime'].dt.day_of_week

        # Y con las variables 'tpep_dropoff_datetime' y 'tpep_pickup_datetime' las usamos para obtener la duracion del viaje en minutos 
        df['trip_duration_minutes'] = round((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60, 1)
        
        # Borramos las columnas que se usaran
        df.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis= 1, inplace=True)
        
        day_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        df['pickup_day_of_week'] = df['pickup_day_of_week'].replace(day_mapping)
        
        # mergeamos la informacion de las zonas de taxis 
        df= pd.merge(df, taxis_zones, left_on='PULocationID', right_on='OBJECTID', how='left')
        
        # Ahora nos quedamos con las columnas que vamos a usar 
        df.drop(['OBJECTID','Shape_Leng','Shape_Area','LocationID'], axis= 1, inplace=True)
        
        # Filtrar datos inválidos
        df = df[(df['fare_amount'] >= 1) & (df['trip_duration_minutes'] >= 1) & (df['trip_distance'] >= 1)]
        
        # Concatenar el resultado con el DataFrame consolidado
        df_consolidado = pd.concat([df_consolidado, df], ignore_index=True)
    
    # Guardar el DataFrame consolidado actualizado
    df_consolidado.to_parquet(archivo_consolidado, index=False)
    return df_consolidado

'''
# Ejemplo de uso:
carpeta = '../Datasets/Henry/' # Carpeta donde estan los archivos 
archivo_base = 'yellow_tripdata_2023-*.parquet'  # Patrón para los archivos a procesar
archivo_consolidado = './datos_limpios/consolidado.parquet'  # ruta y nombre del Archivo consolidado

'''