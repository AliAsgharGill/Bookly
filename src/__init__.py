from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Life span Server is running")
    await init_db()
    yield
    print("Life span Server is shutting down")


version = 1

app = FastAPI(
    title="API",
    description="API for a book review and service",
    version=f"{version}",
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
