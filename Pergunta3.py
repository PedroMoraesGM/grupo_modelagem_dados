import pandas as pd
import streamlit as st

db_delimiter = ";"
df_passagem = pd.read_csv('csv/dim_passagem.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_fatos = pd.read_csv('csv/dim_fatos.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_data = pd.read_csv('csv/dim_data.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)

def pegarLocais():
    return list(set(df_passagem['destino_cidade'].drop(0)))

def calcular_gastos_passagens_por_cidade_por_ano(cidade, ano):
     # Filtrar o dataframe com a cidade selecionada
    df_passagem_por_cidade = df_passagem[df_passagem['destino_cidade'] == cidade]

    # Mesclar o dataframe de passagens com o dataframe de fatos usando dim_passagem_key
    df_merge_fatos = df_passagem_por_cidade.merge(df_fatos, left_on='key_passagem', right_on='dim_passagem_key', how='inner')

     # Mesclar o dataframe mesclado com o dataframe de datas usando dim_data_key
    df_final = df_merge_fatos.merge(df_data, left_on='dim_data_key', right_on='key_data', how='inner')

    # Filtrar o dataframe resultante pelo ano desejado
    df_final_por_ano = df_final[df_final['ano_id'] == int(ano)]

    total_valor_passagem = df_final_por_ano['valor_passagem'].sum()

    return total_valor_passagem