import pandas as pd
import numpy as np 


'''Todas los pasos realizados en este proceso de ETL
estan justificadas en el analisis que se realizo previamente en el 
Anlisis expliratorio de datos(EDA) "Ver en la carpeta de EDA"
'''

def etl_co2_year(co2_year):
    co2_year = co2_year.iloc[:51, [0,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]]
    # Convertimos las columnas como categorías de una sola columna
    lista = co2_year.columns.to_list()[2:]
    co2año = co2_year[["State", 2000]].rename(columns={2000:"CO2"})
    co2año["Year"] = 2000

    for i in lista:
        df = co2_year[["State", i]].rename(columns={i:"CO2"})
        df["Year"] = i
        co2año = pd.concat([co2año, df])
    co2año.to_excel('Datasets_limpios/co2_year_clean.xlsx', index=False)
    return co2año

def etl_co2_transporte(co2transporte):
    co2transporte = co2transporte.iloc[:51, [0,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]]
    # Esto lo aplico al df de transporte
    lista = co2transporte.columns.to_list()[2:]
    co2añot = co2transporte[["State", 2000]].rename(columns={2000:"CO2_transporte"})
    co2añot["Year"] = 2000

    for i in lista:
        df = co2transporte[["State", i]].rename(columns={i:"CO2_transporte"})
        df["Year"] = i
        co2añot = pd.concat([co2añot, df])
    co2añot.to_excel('Datasets_limpios/co2transporte_clean.xlsx', index=False)
    return co2añot

def etl_co2021 (co2021):

    co2021 = co2021.iloc[:51, [0,1,2,3,4,5]]
    co2021.to_excel('Datasets_limpios/co2021_clean.xlsx', index=False)

    return co2021