from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field
from starlette import status

class BOOK:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self,id,title, author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id: int
    title: str =Field(min_length=3)
    author: str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS=[
    BOOK(1,'Computer Science Pro', 'codingwithroby', 'A very nice book!',5),
    BOOK(2,'Be Fast with FastApi', 'codingwithroby', 'A greate book!',5),
    BOOK(3,'Master Endpoints', 'codingwithroby', 'A awesome book!',5),
    BOOK(4,'HP1', 'Author 1', 'Book Description',2),
    BOOK(5,'HP2', 'Author 2', 'Book Description!',3),
    BOOK(6,'HP3', 'Author 3', 'Book Description!',1),
]

app=FastAPI()

app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS
app.get("/books/{book_id}")
async def read_book(book_id: str):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating ==book_rating:
            books_to_return.append(book_rating)
    return books_to_return

app.post('/create-book')
async def create_book(book_request = BookRequest):
    new_book= BOOK(**book_request.dict())
    BOOKS.append(new_book)

