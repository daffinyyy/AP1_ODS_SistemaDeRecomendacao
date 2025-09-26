import streamlit as st
import requests

st.title("Sistema de Recomendação de Livros")

user_id = st.number_input("Digite o ID do usuário:", min_value=1, max_value=3, step=1)

st.button("Recomendar")
    #response = requests.get(f"")
    # if response.status_code == 200:
    #     recomendacoes = response.json()
    #     st.write("Livros recomendados:")
    #     for r in recomendacoes:
    #         st.write(f"- {r['title']} ({r['genre']})")
    # else:
    #     st.error("Erro ao buscar recomendações")
