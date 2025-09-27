from fastapi import FastAPI, HTTPException
from typing import Optional
import pandas as pd
from math import sqrt, pow


def carregar_dataset(caminho='dataset.csv'):
    try:
        df = pd.read_csv(caminho)
        if 'Username' not in df.columns or 'Game' not in df.columns or 'Rating' not in df.columns:
            return pd.DataFrame(columns=["Username", "Game", "Rating"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Username", "Game", "Rating"])

def salvar_dataset(df, caminho='dataset.csv'):
    df.to_csv(caminho, index=False)

def correlacao_pearson(r1, r2):
    soma_xy = soma_x = soma_y = soma_x2 = soma_y2 = 0
    n_comum = 0
    for item in r1:
        if item in r2:
            n_comum += 1
            nota1 = r1[item]
            nota2 = r2[item]
            soma_xy += nota1 * nota2
            soma_x += nota1
            soma_y += nota2
            soma_x2 += pow(nota1, 2)
            soma_y2 += pow(nota2, 2)
    if n_comum == 0:
        return 0
    denom = sqrt(soma_x2 - pow(soma_x, 2) / n_comum) * sqrt(soma_y2 - pow(soma_y, 2) / n_comum)
    if denom == 0:
        return 0
    return (soma_xy - (soma_x * soma_y) / n_comum) / denom

def encontrar_vizinhos_proximos(usuario, df_avaliacoes):
    lista_distancias = []
    aval_usuario = df_avaliacoes[df_avaliacoes['Username'] == usuario].set_index('Game')['Rating'].to_dict()
    for outro_usuario in df_avaliacoes['Username'].unique():
        if outro_usuario != usuario:
            aval_outro = df_avaliacoes[df_avaliacoes['Username'] == outro_usuario].set_index('Game')['Rating'].to_dict()
            dist = correlacao_pearson(aval_usuario, aval_outro)
            lista_distancias.append((dist, outro_usuario))
    lista_distancias.sort(reverse=True)
    return lista_distancias

def gerar_recomendacoes(usuario, df_avaliacoes, jogo_alvo: Optional[str] = None, k=3):
    vizinhos = encontrar_vizinhos_proximos(usuario, df_avaliacoes)
    if not vizinhos:
        return []

    top_vizinhos = vizinhos[:k]
    soma_similaridade = sum(sim for sim, _ in top_vizinhos)
    if soma_similaridade == 0:
        return []

    influencias = {vizinho: sim / soma_similaridade for sim, vizinho in top_vizinhos}

    notas_usuario = df_avaliacoes[df_avaliacoes['Username'] == usuario].set_index('Game')['Rating'].to_dict()
    pontuacoes_jogos = {}

    for sim, vizinho in top_vizinhos:
        notas_vizinho = df_avaliacoes[df_avaliacoes['Username'] == vizinho].set_index('Game')['Rating'].to_dict()
        for jogo, nota in notas_vizinho.items():
            if jogo not in notas_usuario and jogo != "":
                pontuacoes_jogos[jogo] = pontuacoes_jogos.get(jogo, 0) + influencias[vizinho] * nota

    if jogo_alvo:
        return {jogo_alvo: pontuacoes_jogos.get(jogo_alvo, 0)}

    return dict(sorted(pontuacoes_jogos.items(), key=lambda x: x[1], reverse=True))


app = FastAPI(title="Game Recommendation API")

@app.get("/health", tags=["status"])
def health():
    return {"status": "ok"}

@app.get("/recommend/{usuario}", tags=["recommendation"])
def recommend_api(usuario: str, jogo_alvo: Optional[str] = None, k: int = 3):
    df = carregar_dataset()
    if usuario not in df['Username'].unique():
        raise HTTPException(status_code=404, detail=f"Usuário '{usuario}' não encontrado")
    recomendacoes = gerar_recomendacoes(usuario, df, jogo_alvo=jogo_alvo, k=k)
    return recomendacoes
