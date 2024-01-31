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
