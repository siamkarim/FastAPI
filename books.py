from fastapi import FastAPI
from typing import Optional
app = FastAPI()

BOOKS ={
    'book_1': {'title':'title one','author':'author one'},
    'book_2': {'title':'title two','author':'author two'},
    'book_3': {'title':'title three','author':'author three'},
    'book_4': {'title':'title four','author':'author four'},
    'book_5': {'title':'title five','author':'author five'},
}



@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_books(book_name: str ):
    return BOOKS[book_name]
