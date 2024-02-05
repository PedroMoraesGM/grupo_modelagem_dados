import streamlit as st
import datetime
import Pergunta5 as p5
import Pergunta2 as p2
import Pergunta1 as p1
import Pergunta3 as p3

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
    'Qual é o valor total gasto em passagens por cidade em cada ano?',
    'Qual é o valor médio gasto em diárias por local(origem e destino) e período (mês e ano)?',
    'Qual é o valor das despesas de viagens pagas pelos órgãos pagadores em cada ano?'
]

locations_list = ["Brasilia", "Recife", "Pará"] #Substituir pelos dados
cities_list = p2.pegar_todas_cidades()
period_list = ["2021", "2022", "2023"] 
min_date = datetime.date(2021, 1, 1)
max_date = datetime.date(2023, 12, 31)

opcao_pergunta = st.selectbox(
    'Selecione a pergunta: ',
    perguntas
)

def formatar_valor(valor):
    # Formatando o valor como uma soma de dinheiro
    return '{:,.2f}'.format(valor).replace(',', ' ').replace('.', ',').replace(' ', '.')

def valor_total_diarias_passagens_outros_local_periodo():
    st.subheader("Abaixo é possível regular alguns filtros para obter melhores observações:")
    st.write("Qual foi o valor total gasto somando diárias, passagens e outros, em cada local e período?")
    selected_location = st.selectbox("Escolha o local", cities_list)
    start_date = st.date_input("Determine o período de início", value=(datetime.date(2021, 1, 1)), min_value=min_date, max_value=max_date)
    end_date = st.date_input("Determine o fim do período", value=(datetime.date(2023, 1, 31)), min_value=min_date, max_value=max_date)

    # Calcular e exibir o valor total
    total_cidade_periodo = p1.calcular_total_cidade_periodo(selected_location, start_date, end_date)
    total_formatado = formatar_valor(total_cidade_periodo)
    st.subheader(f'O custo total para a cidade de {selected_location} no período de {start_date} a {end_date} é: R$ {total_formatado}')

def valor_total_diarias_passagens_outros_cidade():
    st.subheader(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.write(
    "Qual foi o valor total gasto somando diárias, passagens e outros por cidade?"
    )
    selected_location = st.selectbox("Escolha a cidade", cities_list)

    # Obter o valor total gasto pela cidade selecionada
    valor_total = p2.calcular_total_cidade(selected_location)

    valor_formatado = formatar_valor(valor_total)

    st.subheader(f"O valor total gasto em {selected_location} foi {valor_formatado}")


def valor_total_passagens_cidade_pais_ano():
    st.write(
    "Abaixo é possível regular alguns filtros para obter melhores observações:"
    )
    st.subheader(
    "Qual foi o valor total gasto em passagens por cidade em cada ano?"
    )
    selected_location = st.selectbox("Escolha o local", p3.pegarLocais())
    selected_year = st.selectbox("Escolha o ano", period_list)
    valor_total_passagens = p3.calcular_gastos_passagens_por_cidade_por_ano(selected_location, selected_year)
    if(valor_total_passagens != int(0)):
        total_formatado = f'R$ {valor_total_passagens:,.2f}'.replace(',', 'v').replace('.', ',').replace('v', '.')
        st.write(f"Valor total gasto em passagens para {selected_location} no ano de {selected_year} foi de: {total_formatado}")
    else:
        st.warning("Não há registros para esses valores")

    


    

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
    orgao = st.selectbox("Escolha o orgao", p5.pegar_todos_nomes_orgao())
    ano = st.selectbox("Escolha o ano", p5.pegar_anos_de_pagamento(orgao))
    p5.pegar_pagamentos_orgao_por_ano(orgao, ano)

if opcao_pergunta == perguntas[0]:
    valor_total_diarias_passagens_outros_local_periodo()
elif opcao_pergunta == perguntas[1]:
    valor_total_diarias_passagens_outros_cidade()
elif opcao_pergunta == perguntas[2]:
    valor_total_passagens_cidade_pais_ano()
elif opcao_pergunta == perguntas[3]:
    valor_medio_diarias_local_periodo()
elif opcao_pergunta == perguntas[4]:
    despesas_viagens_orgaos_periodo()
