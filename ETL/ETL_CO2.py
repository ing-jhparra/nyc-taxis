import pandas as pd

def EtlCo2(df):
    df.drop(['Percent','Absolute','Percent.1', 'Absolute.1'], axis=1, inplace=True)
    df_long = pd.melt(df, id_vars=['State'],
                    var_name='Year', value_name='CO2')
    df_long = df_long[(df_long['Year'] >= 2000) & (df_long['State'] != 'Total of states')]
    
    return df_long

def EtlTransporteCo2(df):
    df.drop(['Percent','Absolute'], axis=1, inplace= True)
    df_long = pd.melt(df, id_vars=['State'],
                    var_name='Year', value_name='CO2')
    df_long = df_long[(df_long['Year'] >= 2000) & (df_long['State'] != 'State total1')]
    
    return df_long

def EtlCo2021(df):
    df = df.iloc[:51, [0,1,2,3,4,5]]

    return df