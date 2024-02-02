import pandas as pd

def ler_dataframe(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df

def filtrar_dataframe_por_coluna(df, coluna, valor):
    df_filtrado = df[df[coluna] == valor]
    return df_filtrado
