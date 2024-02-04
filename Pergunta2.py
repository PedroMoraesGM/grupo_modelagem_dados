import pandas as pd
import streamlit as st

db_delimiter = ";"

df_passagem = pd.read_csv('csv/dim_passagem.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)

df_pagamento = pd.read_csv('csv/dim_pagamento.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)

def pegar_todas_cidades():
    return df_passagem['origem_cidade']

def calcular_total_cidade(cidade):
    custoTotal = 0
    
    # Filtrar as linhas de dim_pagamento relacionadas à cidade
    linhas_cidade = df_passagem[df_passagem['origem_cidade'] == cidade]['tb_viagem_id_viagem']
    
    # Filtrar dim_pagamento com base nas linhas encontradas
    df_pagamento_cidade = df_pagamento[df_pagamento['tb_viagem_id_viagem'].isin(linhas_cidade)]
    
    # Calcular a soma dos valores
    custoTotal = df_pagamento_cidade['valor_diarias'].sum() + df_pagamento_cidade['valor_passagens'].sum() + df_pagamento_cidade['valor_outros'].sum()

    return custoTotal

