import streamlit as st
import requests

url = "http://127.0.0.1:8000/recommend"

logo_normal = "frontend/assets/logo_sapo.png"
logo_buscar = "frontend/assets/logo_busca.png"


#mudando cor de fundo
st.markdown(
    """
    <style>
    .stApp {
        background-color: #53853e;
    }

    .stButton button {
        background-color: #3c5e2d;
        color: white;
    }

    div.stTextInput>div>div>input {
        background-color: #ffffcc;  /* amarelo clarinho */
        color: #333333;             
        border-radius: 8px;        
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#cabeçalho com logo e nome
col1, col2 = st.columns([1, 3])
with col1:
    logo_placeholder = st.empty()
    logo_placeholder.image(logo_normal, width=200)
with col2:
    st.title("S.A.P.O. – Sistema de Avaliação de Preferências de Obras")


#imput do usuário
book_title = st.text_input("Digite o título do livro que acabou de ler:")

#botão
if st.button("Buscar"):
    logo_placeholder.image(logo_buscar, width=200)

    payload = {"book_title": book_title} 
    response = requests.post(url, json=payload)

    logo_placeholder.image(logo_normal, width=200)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if not results:
            st.warning("Nenhum livro encontrado.")
        else:
            st.subheader("Resultados recomendados:")
            for r in results:
                col1, col2 = st.columns([1, 3]) #capa e infos

                with col1: #pra capa
                    if r.get("image_url"):
                        st.image(r["image_url"], width=110)

                with col2: #pra info
                    st.write(f"**{r['title']}**")
                    if r.get("author"):
                        st.write(f"*Autor:* {r['author']}")
                    if r.get("year"):
                        st.write(f"Ano de publicação: {r['year']}")
                    if r.get("publisher"):
                        st.write(f"Editora: {r['publisher']}")
                    st.markdown("---")
    else:
        st.error("Erro na API")
