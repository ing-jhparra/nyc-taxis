import pandas as pd
import numpy as np 
import os
import glob

'''Todas los pasos realizados en este proceso de ETL
estan justificadas en el analisis que se realizo previamente en el 
Anlisis expliratorio de datos(EDA) "Ver en la carpeta de EDA"
'''

def EtlTaxisTrip(carpeta, archivo_base, sample_size=100000):
    
    # Obtener todos los archivos que coincidan con el patrón
    all_files = glob.glob(os.path.join(carpeta, archivo_base))
    df_consolidado = pd.DataFrame()
    
    for file in all_files:
        if not os.path.exists(file):
            print(f"Archivo no encontrado: {file}")
            continue
        
        df = pd.read_parquet(file)
        
        # Verificar si el tamaño del muestreo no excede el número de filas del archivo 
        sample_size = min(sample_size, len(df))
        random_indices = np.random.choice(df.index, size=sample_size, replace=False)
        df = df.loc[random_indices]
        
        # Seleccionar columnas a utilizar 
        df = df[['tpep_pickup_datetime','tpep_dropoff_datetime','trip_distance','fare_amount']]
        
        # Convertir a datetime si no están en ese formato
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        
        # Calcular duración del viaje a minutos 
        df['trip_duration_minutes'] = round((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60, 1)
        
        # Borramos las columnas que se usaran
        df.drop(['tpep_pickup_datetime','tpep_dropoff_datetime'], axis= 1, inplace=True)
        
        # Filtrar datos inválidos
        df = df[(df['fare_amount'] >= 1) & (df['trip_duration_minutes'] >= 1) & (df['trip_distance'] >= 1)]
        
        # Aplicar límites para cada columna una vez, no dentro de un bucle
        for column in ['fare_amount', 'trip_distance', 'trip_duration_minutes']:
            media = df[column].mean()
            desviacion = df[column].std()
            limite_inferior = media - 2 * desviacion
            limite_superior = media + 2 * desviacion
            df = df[(df[column] >= limite_inferior) & (df[column] <= limite_superior)]
        
        # Concatenar el resultado con el DataFrame consolidado
        df_consolidado = pd.concat([df_consolidado, df], ignore_index=True)
    
    return df_consolidado