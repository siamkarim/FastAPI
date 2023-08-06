from fastapi import FastAPI

app = FastAPI()

BOOKS ={
    'book_1':{'title':'title one','author':'author one'},
    'book_2':{'title':'title two','author':'author two'},
    'book_3':{'title':'title three','author':'author three'},
    'book_4':{'title':'title four','author':'author four'},
    'book_5':{'title':'title five','author':'author five'},
}

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/books/mybooks")
async def my_favourite_books():
    return {"book_title": "my favourite books"}

@app.get("/books/{book_id}")
async def read_books(book_id: int):
    return {"book_title": book_id}
