from pydantic import BaseModel
from typing import List, Optional

class RecommendationRequest(BaseModel):
    '''
    pede os 5 livros mais parecidos
    '''
    category:str
    top_n: int = 5

class BookInfo(BaseModel):
    '''
    estrutura de infos do livro
    '''
    title: str
    subtitle: Optional[str] = None
    authors: Optional[str] = None
    categories: str
    average_rating: float
    published_year: int
    description: Optional[str] = None

class RecommendationResponse(BaseModel):
    '''
    responde o livro
    '''
    results: List[BookInfo]
