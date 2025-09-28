from pydantic import BaseModel
from typing import List, Optional

class RecommendationRequest(BaseModel):
    '''
    pede os 5 livros mais parecidos
    '''
    book_isbn:str
    top_n: int = 5

class BookInfo(BaseModel):
    '''
    estrutura de infos do livro
    '''
    isbn: str
    title: str
    author: Optional[str] = None
    year: Optional[int] = None
    publisher: Optional[str] = None
    image_url: Optional[str] = None

class RecommendationResponse(BaseModel):
    '''
    responde o livro
    '''
    results: List[BookInfo]
