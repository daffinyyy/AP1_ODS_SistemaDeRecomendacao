from fastapi import FastAPI
import pandas as pd
from backend.models import RecommendationResponse, RecommendationRequest, BookInfo
from backend.funcao_de_recomendacao import recommend_by_category


app = FastAPI (
    title="Book Recommendation API",
)

@app.get("/health", tags=["status"])
def health() -> dict:
    return {"status": "ok"}

#post da API
@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest):
    """
    recomendação por categoria
    """
    # alterar pro atual nome da função dps
    results_df = recommend_by_category(request.category, top_n=request.top_n)

    #possiveis erros
    if isinstance(results_df, str):
        return {"error": results_df} 

    results = [
    BookInfo(
        title=row["title"],
        subtitle=None if pd.isna(row.get("subtitle")) else row.get("subtitle"),
        authors=None if pd.isna(row.get("authors")) else row.get("authors"),
        categories=row["categories"],
        average_rating=float(row["average_rating"]),
        published_year=int(row["published_year"]),
        description=None if pd.isna(row.get("description")) else row.get("description")
    )
    for _, row in results_df.iterrows()
]

    return {"results": results}