import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#datasets
books = pd.read_csv("backend/data/BX-Books.csv", sep=";", encoding="latin-1")
ratings = pd.read_csv("backend/data/BX-Book-Ratings-Subset.csv", sep=";", encoding="latin-1")
item_user_matrix = ratings.pivot(index='ISBN', columns='User-ID', values='Book-Rating').fillna(0)

#calculo da similaridade
similarity_matrix = cosine_similarity(item_user_matrix)
similarity_df = pd.DataFrame(similarity_matrix, index=item_user_matrix.index, columns=item_user_matrix.index)

def recommend_item_based(book_isbn, top_n=5):
    '''
    recomendação baseada em item
    '''
    if book_isbn not in similarity_df.index:
        return "Livro não encontrado"
    
    # pega os livros mais similares
    similar_scores = similarity_df[book_isbn].sort_values(ascending=False).head(top_n + 1)
    similar_scores = similar_scores.drop(book_isbn)

    
    # retorna os dados dos livros similares
    return books[books['ISBN'].isin(similar_scores.index)][
        ['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-M']
    ]

