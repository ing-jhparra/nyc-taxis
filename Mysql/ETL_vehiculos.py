import os
import glob
import pandas as pd
import warnings
# Suprimir todas las advertencias
warnings.filterwarnings("ignore")



def etl_fuel():

    # Ruta de los archivos
    path = 'Datasets'

    # Patrones de archivo
    all_files = glob.glob(os.path.join(path, 'my*-fuel-consumption-ratings*.csv'))

    # Lista para almacenar los DataFrames individuales
    df_list = []

    # Leer y combinar los archivos CSV en un solo DataFrame
    for file in all_files:
        df = pd.read_csv(file, encoding='latin1')
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    # Filtrar los datos para eliminar los años anteriores a 2012
    filtered_df = combined_df[combined_df['Model year'] >= 2012]

    # Agregar la columna 'Tipo de Vehículo' con el valor 'Fuel'
    filtered_df['CO2 rating'].fillna(filtered_df['CO2 rating'].mean().astype(int), inplace=True)
    filtered_df['Smog rating'].fillna(filtered_df['Smog rating'].mean().astype(int), inplace=True)

    # Mostrar el DataFrame resultante
    filtered_df = filtered_df.drop(columns=['Engine size (L)', 'Cylinders','Transmission','Fuel type','City (L/100 km)','Highway (L/100 km)','Combined (mpg)'])
    filtered_df.to_csv('Datasets_limpios/vehículo_fuel_clean.csv', index=False)
    return filtered_df    

def etl_electrico(df_electrico):
    #df_electrico=pd.read_csv('Dataset/link/my2012-2024-battery-electric-vehicles.csv')
    df_electrico = df_electrico.drop(columns=['City (kWh/100 km)', 'Highway (kWh/100 km)','Transmission','Fuel type','City (Le/100 km)','Highway (Le/100 km)','Combined (Le/100 km)','Motor (kW)'])
    df_electrico['CO2 rating '] = '0'
    df_electrico['Smog rating'].fillna(df_electrico['Smog rating'].mean().astype(int), inplace=True)
    df_electrico.to_csv('Datasets_limpios/vehículo_electrico_clean.csv', index=False)
    return df_electrico  


def etl_hibrido(df_hibrido):
    #df_hibrido=pd.read_csv('Dataset/link/my2012-2024-plug-in-hybrid-electric-vehicles.csv')
    df_hibrido['CO2 rating'].fillna(df_hibrido['CO2 rating'].mean().astype(int), inplace=True)
    df_hibrido['Smog rating'].fillna(df_hibrido['Smog rating'].mean().astype(int), inplace=True)
    df_hibrido = df_hibrido.drop(columns=['Engine size (L)', 'Cylinders','Transmission','Fuel type 1','Fuel type 2','City (L/100 km)','Highway (L/100 km)','Motor (kW)','Combined Le/100 km'])
    df_hibrido.to_csv('Datasets_limpios/vehículo_hibrido_clean.csv', index=False)
    return df_hibrido