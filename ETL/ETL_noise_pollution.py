import pandas as pd
import pandas as pd
import numpy as np 
from datetime import datetime, timedelta

df = pd.read_csv('../Datasets/annotations.csv')

def noise_pollution(df):

    ## Esta función convierte los valores de año, semana y día en una fecha
    def year_week_day_to_date(row):
        year = int(row['year'])
        week = int(row['week'])
        day = int(row['day'])
        # Definir el primer día del año
        first_day_of_year = datetime(year, 1, 1)
        # Añadir el número de semanas y días
        return first_day_of_year + timedelta(weeks=week-1, days=day)

    # Crear una nueva columna 'date' usando la función
    df['date'] = df.apply(year_week_day_to_date, axis=1)

    # Extraer el mes de la columna 'date'
    df['month'] = df['date'].dt.month

    #Seleccionamos la columnas relevantes para el análisis
    df = df[['date', 'day', 'month', 'year', 'hour',
                            'borough', 'latitude', 'longitude', '1_engine_presence']]

    return df    
