import streamlit as st
import requests

st.title("Sistema de Recomendação de Cerveja")

user_id = st.number_input("Digite o ID do usuário:", min_value=1, max_value=3, step=1)

st.button("Recomendar")
    #response = requests.get(f"http://127.0.0.1:5000/recomendar/{user_id}")
    # if response.status_code == 200:
    #     recomendacoes = response.json()
    #     st.write("Filmes recomendados:")
    #     for r in recomendacoes:
    #         st.write(f"- {r['title']} ({r['genre']})")
    # else:
    #     st.error("Erro ao buscar recomendações")
