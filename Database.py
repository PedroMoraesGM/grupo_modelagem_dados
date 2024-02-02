import pandas as pd

csv_data = "dim_data.csv"
csv_orgao = "dim_orgao.csv"
csv_pagamento = "dim_pagamento.csv"
csv_passagem = "dim_passagem.csv"
csv_viagem = "dim_viagem.csv"
csv_fatos = "dim_fatos.csv"

def ler_dataframe(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    return df

def filtrar_dataframe_por_coluna(df, coluna, valor):
    df_filtrado = df[df[coluna] == valor]
    return df_filtrado

caminho_arquivo = 'caminho/do/seu/arquivo.csv'
df = ler_dataframe(caminho_arquivo)

df_filtrado = filtrar_dataframe_por_coluna(df, 'idade', 25)