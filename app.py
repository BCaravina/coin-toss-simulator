import streamlit as st

st.header("Jogando uma moeda")

# adicionando controle deslizante para selecionar qtde de tentativas
number_of_trials = st.slider("Número de tentativas?", 1, 1000, 10)
start_button = st.button("Executar")

if start_button:
    st.write(f"Executando o experimento de {number_of_trials} tentativas.")

st.write("Ainda não é um aplicativo funcional. Em construção.")
