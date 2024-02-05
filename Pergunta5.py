import pandas as pd
import streamlit as st

db_delimiter = ";"
df_data = pd.read_csv('csv/dim_data.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_fatos = pd.read_csv('csv/dim_fatos.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)
df_orgao = pd.read_csv('csv/dim_orgao.csv', encoding='latin-1', on_bad_lines='skip', delimiter=db_delimiter)

def pegar_todos_nomes_orgao():
    return df_orgao['nome_orgao'].drop(0)

def pegar_anos_de_pagamento(orgao):
    
    # Encontrar o ID do órgão desejado
    id_orgao_selecionado = df_orgao[df_orgao['nome_orgao'] == orgao]['id_orgao'].values[0]

    # Filtrar o dataframe apenas com o órgão desejado
    df_orgao_filtrado = df_fatos[df_fatos['dim_orgao_key_pagador'] == id_orgao_selecionado]

    # Merge no dataframe de Fatos e Data utilizando as colunas relacionadas à data
    df_merge_data_orgao = pd.merge(df_orgao_filtrado, df_data, left_on='dim_data_key', right_on="key_data", right_index=True)

    # Filtrar o novo dataframe apenas com registros que ocorreram no ano selecionado
    return df_merge_data_orgao['ano_id'].unique()

def pegar_pagamentos_orgao_por_ano(orgao_selecionado, ano_selecionado):

    # Encontrar o ID do órgão desejado
    id_orgao_selecionado = df_orgao[df_orgao['nome_orgao'] == orgao_selecionado]['id_orgao'].values[0]

    # Filtrar o dataframe apenas com o órgão desejado
    df_orgao_filtrado = df_fatos[df_fatos['dim_orgao_key_pagador'] == id_orgao_selecionado]

    # Merge no dataframe de Fatos e Data utilizando as colunas relacionadas à data
    df_merge_data_orgao = pd.merge(df_orgao_filtrado, df_data, left_on='dim_data_key', right_on="key_data", right_index=True)

    # Filtrar o novo dataframe apenas com registros que ocorreram no ano selecionado
    df_ano_filtrado = df_merge_data_orgao[df_merge_data_orgao['ano_id'] == ano_selecionado]

    if df_ano_filtrado.empty:
        st.warning("Não há registros para este ano")
    else:

        # Converter valores do dataframe para numérico
        df_ano_filtrado = df_ano_filtrado[['diarias', 'passagens', 'outros']].apply(pd.to_numeric, errors='coerce')

        # Somar os custos e criar nova coluna
        df_ano_filtrado['Total'] = df_ano_filtrado.sum(axis=1)
        
        gasto_total_no_ano = df_ano_filtrado['Total'].sum()

        # Renomear as colunas para melhor entendimento
        df_ano_filtrado = df_ano_filtrado.rename(columns={'diarias': 'Diárias', 'passagens': 'Passagens', 'outros': 'Outros'})

        # Formatar valores
        df_ano_filtrado[['Diárias', 'Passagens', 'Outros', 'Total']] = df_ano_filtrado[['Diárias', 'Passagens', 'Outros', 'Total']].applymap(lambda x: f'R$ {x:,.2f}' if isinstance(x, (int, float)) else x)

        # Ordenar pelo total
        df_ano_filtrado = df_ano_filtrado.sort_values(by='Total')

        # Detalhamento dos custos de cada viagem
        #st.dataframe(df_ano_filtrado[['Diárias', 'Passagens', 'Outros', 'Total']], hide_index=True, use_container_width=True)

        # Mostra a soma total
        total_formatado = f'R$ {gasto_total_no_ano:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')
        st.write(f"A soma total dos gastos é: {total_formatado}")
