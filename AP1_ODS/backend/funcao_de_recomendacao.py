import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("backend\data\data.csv")

#transformando em vetor
vectorizer = CountVectorizer(binary=True, token_pattern=r'[^,]+')
X = vectorizer.fit_transform(data['categories'].fillna(""))

#similaridade cosseno
similaridade = cosine_similarity(X)
similaridade = pd.DataFrame(similaridade, index=data['title'], columns=data['title'])

def recommend_by_category(book_title, top_n=5):
    """
    retorna uma lista de livros com as categorias mais parecidas.

    book_title: título do livro base para a recomendação
    top_n: número de recomendações
    """
    if book_title not in similaridade.index:
        return "Livro não encontrado."

    #ordena pela similaridade e pega os melhores
    similares = similaridade[book_title].sort_values(ascending=False)
    top_books = similares.drop(book_title).head(top_n)  #ignora a si mesmo

    # Retorna informações úteis (pode ajustar as colunas que quiser)
    return data[data['title'].isin(top_books.index)][
        ['title', 'subtitle', 'authors', 'categories', 'average_rating', 'published_year', 'description']
    ]
