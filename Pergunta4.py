import datetime
import pandas as pd
import streamlit as st

db_delimiter = ";"

df_passagem = pd.read_csv('csv/dim_passagem.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_pagamento = pd.read_csv('csv/dim_pagamento.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_viagem = pd.read_csv('csv/dim_viagem.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)

def pegar_todas_cidades():
    return df_passagem['origem_cidade']

def formatar_valor(valor):
    # Formatando o valor como uma soma de dinheiro
    return '{:,.2f}'.format(valor).replace(',', ' ').replace('.', ',').replace(' ', '.')

def calcular_media_diarias_cidade_periodo(cidade, inicio_periodo, fim_periodo):
    mediaDiarias = 0
    
    # Convertendo os valores de início e fim do período para o formato datetime.date
    inicio_periodo = datetime.datetime.strptime(str(inicio_periodo), '%Y-%m-%d').date()
    fim_periodo = datetime.datetime.strptime(str(fim_periodo), '%Y-%m-%d').date()
    
    # Convertendo as colunas de inicio_viagem e fim_viagem para datetime.date no DataFrame
    df_viagem['inicio_viagem'] = pd.to_datetime(df_viagem['inicio_viagem']).dt.date
    df_viagem['fim_viagem'] = pd.to_datetime(df_viagem['fim_viagem']).dt.date
    
    # Filtrar as linhas de dim_viagem relacionadas ao período
    linhas_periodo = df_viagem[(df_viagem['inicio_viagem'] >= inicio_periodo) & (df_viagem['fim_viagem'] <= fim_periodo)]['id_viagem']
    
    # Filtrar dim_passagem com base nas linhas encontradas
    linhas_cidade_periodo = df_passagem[(df_passagem['origem_cidade'] == cidade) & 
                                         (df_passagem['tb_viagem_id_viagem'].isin(linhas_periodo))]['tb_viagem_id_viagem']
    
    # Filtrar dim_pagamento com base nas linhas encontradas
    df_pagamento_cidade_periodo = df_pagamento[df_pagamento['tb_viagem_id_viagem'].isin(linhas_cidade_periodo)]
    
    # Calcular a média dos valores de diárias
    if not df_pagamento_cidade_periodo.empty:
        mediaDiarias = df_pagamento_cidade_periodo['valor_diarias'].mean()

    return mediaDiarias
