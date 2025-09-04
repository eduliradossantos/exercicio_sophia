import streamlit as st
import pandas as pd

st.title("SofIA - Introdução ao Streamlit")

st.write("Bem-vindos à nossa aula sobre **Streamlit**: criando interfaces rápidas em Python!")

st.sidebar.title("Menu Lateral")

pagina = st.sidebar.radio("Escolha:",["Cadastro", "Upload","Gráficos"])

if pagina == "Cadastro":
    st.write("Você está na página inicial")
    st.title("Widgets")
    nome = st.text_input("Digite seu nome:")

elif pagina == "Upload":
    st.write("Informações sobre o app.")
    st.title("Upload de Arquivos")
    arquivo = st.file_uploader("Envie um arquivo CSV")
    if arquivo:
        df = pd.read_csv(arquivo)
        st.dataframe(df)

else:
    dados = pd.DataFrame({
        "Alunos":["Ana","Bruno","Carlos","Diana"],
        "Notas":[8.5, 7.0, 9.2, 6.8]
    })
    st.bar_chart(dados.set_index("Alunos"))