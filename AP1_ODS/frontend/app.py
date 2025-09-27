import streamlit as st
import requests

url = "http://127.0.0.1:8000/recommend"

st.title("Sistema de Recomendação de Livros")

#imput do usuário
category = st.text_input("Digite um livro que acabou de ler:")

#botão de recomendação
if st.button("Recomendar"):
    payload = {"category": category}  #o nome precisa bater com o RecommendationRequest
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        results = response.json()["results"]
        st.subheader("Resultados:")
        for r in results:
            st.write(f"**{r['title']}**")

            if r.get("subtitle"):
                st.write(f"*{r['subtitle']}*")

            if r.get("authors"):
                st.write(f"Autor(es): {r['authors']}")

            st.write(f"Categoria(s): {r['categories']}")

            st.write(f"Nota: {r['average_rating']}")

            st.write(f"Ano de publicação: {r['published_year']}")

            if r.get("description"):
                st.write(f"Descrição: {r['description']}")

            st.markdown("---")
    else:
        st.error("Erro na API")