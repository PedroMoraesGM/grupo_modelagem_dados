import streamlit as st

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

locations_list = ["Brasilia", "Recife", "Pará"]

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
    selected_period = st.selectbox("Determine um periodo", locations_list)

if opcao_pergunta == perguntas[0]:
    valor_total_diarias_passagens_outros_local_periodo()
