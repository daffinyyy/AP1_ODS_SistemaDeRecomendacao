from fastapi import FastAPI
import pandas as pd
from backend.models import RecommendationResponse, RecommendationRequest, BookInfo
from backend.funcao_de_recomendacao import recommend_item_based, books


app = FastAPI (
    title="Book Recommendation API",
)

@app.get("/health", tags=["status"])
def health() -> dict:
    return {"status": "ok"}

#post da API
@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    results_df = recommend_item_based(request.book_isbn, top_n=request.top_n)

    if isinstance(results_df, str):
        return {"results": []}  #se não encontrar retorna lista vazia

    results = [
        BookInfo(
            isbn=row["ISBN"],
            title=row["Book-Title"],
            author=row["Book-Author"],
            year=int(row["Year-Of-Publication"]),
            publisher=row["Publisher"],
            image_url=row["Image-URL-M"]
        )
        for _, row in results_df.iterrows()
    ]

    return {"results": results}