from fastapi import APIRouter

book_router = APIRouter()

@book_router.get("/")
def get_books():
    return {"message": "List of books"}
