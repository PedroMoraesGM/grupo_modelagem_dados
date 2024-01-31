import streamlit as st
import datetime

st.set_page_config(
    page_title = "Viagens gov",
    layout = "wide",
    menu_items = {
        'About': ''' 
        '''
    }
)

st.markdown(f'''
    <h1>Analise de Data Warehouse dos dados de viagens do portal do governo </h1>
    <br>
    <p>
        Este projeto tem o objetivo de analisar, por meio de plotagem de gráficos, os dados de viagens a servico do governo.
        Está sendo desenvolvido para a disciplina de Modelagem de Dados da Universidade Federal Rural de Pernambuco, pelos graduandos:
    </p>
    <br>
    <ul>
        <li>Arthur Estevao</li>
        <li>Marcos Moraes</li>
        <li>Pedro Moraes</li>
        <li>Sergio Filho</li>
    </ul>
    <br>
''', unsafe_allow_html=True)

perguntas = [
    'Qual é o valor total gasto em diárias, passagens e outros gastos por local e períodos', 
    'Qual é o valor total gasto em diárias, passagens e outros gastos por cidade?',
    'Qual é o valor total gasto em diárias por cidade/país por ano?',
    'Qual é o valor médio gasto em diárias por local(origem e destino) e período (mês e ano)?',
    'Qual é o valor das despesas de viagens pagas pelos órgãos pagadores em cada ano?'
]

locations_list = ["Brasilia", "Recife", "Pará"] #Substituir pelos dados
parties_list = ["PT", "PSD", "CDB"] #Substituir pelos dados
period_list = ["2021", "2022", "2023"] 

min_date = datetime.date(2021, 1, 1)
max_date = datetime.date(2023, 12, 31)

opcao_pergunta = st.selectbox(
    'Selecione a pergunta: ',
    perguntas
)

def valor_total_diarias_passagens_outros_local_periodo():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor total gasto somando diárias, passagens e outros, em cada local e periodo?"
    )
    selected_location = st.selectbox("Escolha o local", locations_list)
    start_date = st.date_input(
        "Determine o periodo de inicio",
        value=(datetime.date(2021, 1, 1)),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY"
    )
    end_date = st.date_input(
        "Determine o fim do periodo",
        value=(datetime.date(2023, 1, 31)),
        min_value=min_date,
        max_value=max_date,
        format="MM/DD/YYYY"
    )

def valor_total_diarias_passagens_outros_cidade():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor total gasto somando diárias, passagens e outros por cidade?"
    )
    selected_location = st.selectbox("Escolha a cidade", locations_list)

def valor_total_diarias_cidade_pais_ano():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor total gasto somando diárias por cidade e ano?"
    )
    selected_location = st.selectbox("Escolha o local", locations_list)
    selected_year = st.selectbox("Escolha o ano", period_list)

def valor_medio_diarias_local_periodo():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor medio gasto em diárias por local e periodo?"
    )
    selected_location = st.selectbox("Escolha o local", locations_list)

    start_date = st.date_input(
        "Determine o periodo de inicio",
        value=(datetime.date(2021, 1, 1)),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY"
    )
    end_date = st.date_input(
        "Determine o fim do periodo",
        value=(datetime.date(2023, 1, 31)),
        min_value=min_date,
        max_value=max_date,
        format="MM/DD/YYYY"
    )

def valor_medio_diarias_local_periodo():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor medio gasto em diárias por local e periodo?"
    )
    selected_location = st.selectbox("Escolha o local", locations_list)

    start_date = st.date_input(
        "Determine o periodo de inicio",
        value=(datetime.date(2021, 1, 1)),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY"
    )
    end_date = st.date_input(
        "Determine o fim do periodo",
        value=(datetime.date(2023, 1, 31)),
        min_value=min_date,
        max_value=max_date,
        format="MM/DD/YYYY"
    )

def despesas_viagens_orgaos_periodo():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor das despesas de viagens pagas pelos órgãos pagadores por ano?"
    )
    selected_location = st.selectbox("Escolha o orgao", parties_list)

    start_date = st.date_input(
        "Determine o periodo de inicio",
        value=(datetime.date(2021, 1, 1)),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY"
    )
    end_date = st.date_input(
        "Determine o fim do periodo",
        value=(datetime.date(2023, 1, 31)),
        min_value=min_date,
        max_value=max_date,
        format="MM/DD/YYYY"
    )

if opcao_pergunta == perguntas[0]:
    valor_total_diarias_passagens_outros_local_periodo()
elif opcao_pergunta == perguntas[1]:
    valor_total_diarias_passagens_outros_cidade()
elif opcao_pergunta == perguntas[2]:
    valor_total_diarias_cidade_pais_ano()
elif opcao_pergunta == perguntas[3]:
    valor_medio_diarias_local_periodo()
elif opcao_pergunta == perguntas[4]:
    despesas_viagens_orgaos_periodo()
