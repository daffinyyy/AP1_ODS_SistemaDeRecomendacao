import pandas as pd
from sklearn.model_selection import train_test_split
from backend.funcao_de_recomendacao import recommend_item_based, ratings

ratings = pd.read_csv("backend/data/BX-Book-Ratings-Subset.csv", sep=";", encoding="latin-1")

#teste esparsidade
# item_user_matrix = ratings.pivot(index='ISBN', columns='User-ID', values='Book-Rating').fillna(0)
# total_elements = item_user_matrix.size
# non_zero = (item_user_matrix != 0).sum().sum()
# sparsity = 1 - (non_zero / total_elements)
# print(f"Esparsidade da matriz: {sparsity:.2%}")

#identifica usuário com mais avaliações
avaliacoes_por_usuario = ratings.groupby("User-ID").size()
usuario_mais_ativo = avaliacoes_por_usuario.idxmax()
print(f"Usuário selecionado: {usuario_mais_ativo} ({avaliacoes_por_usuario.max()} avaliações)")

avaliacoes_usuario = ratings[ratings["User-ID"] == usuario_mais_ativo]

#divisao dos dados
train, test = train_test_split(avaliacoes_usuario, test_size=0.5, random_state=42)

#PT 1. gerando as recomendações 
train_isbns = train["ISBN"].tolist() 
recomendados = set() 

for isbn in train_isbns: 
    if isbn in recommend_item_based.__globals__["similarity_df"].index: 
        recs_df = recommend_item_based(isbn, top_n=5) 
        recomendados.update(recs_df["ISBN"].tolist())

#PT 2. comparando com oq ele realmente gostou
test_gostou = set(test.query("`Book-Rating` >= 7")["ISBN"].tolist())

#calculo da acuracia
matches = len(recomendados & test_gostou)
total_recomendados = len(recomendados)
acuracia = matches / total_recomendados

print(f"Total de recomendações geradas: {total_recomendados}")
print(f"Número de acertos (matches): {matches}")
print(f"Acurácia: {acuracia*100:.2f}%")
