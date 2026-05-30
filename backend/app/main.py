from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware

from .data import BOOKS
from .models import Book, BookCreate, LibraryStats

app = FastAPI(
    title="Electronic Library API",
    description="Prototype backend for an electronic library application.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "electronic-library-backend"}


@app.get("/api/books", response_model=list[Book])
def get_books(
    search: str | None = Query(default=None, description="Search by title, author or description"),
    category: str | None = Query(default=None, description="Filter by category"),
    language: str | None = Query(default=None, description="Filter by language"),
) -> list[Book]:
    result = BOOKS

    if search:
        query = search.lower().strip()
        result = [
            book
            for book in result
            if query in book.title.lower()
            or query in book.description.lower()
            or any(query in author.lower() for author in book.authors)
        ]

    if category and category != "all":
        result = [book for book in result if book.category == category]

    if language and language != "all":
        result = [book for book in result if book.language == language]

    return result


@app.get("/api/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/api/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate) -> Book:
    new_id = max((item.id for item in BOOKS), default=0) + 1
    new_book = Book(id=new_id, **book.model_dump())
    BOOKS.append(new_book)
    return new_book


@app.get("/api/categories", response_model=list[str])
def get_categories() -> list[str]:
    return sorted({book.category for book in BOOKS})


@app.get("/api/languages", response_model=list[str])
def get_languages() -> list[str]:
    return sorted({book.language for book in BOOKS})


@app.get("/api/stats", response_model=LibraryStats)
def get_stats() -> LibraryStats:
    total_books = len(BOOKS)
    available_copies = sum(book.available_copies for book in BOOKS)
    average_rating = round(sum(book.rating for book in BOOKS) / total_books, 2) if total_books else 0
    return LibraryStats(
        total_books=total_books,
        total_categories=len({book.category for book in BOOKS}),
        available_copies=available_copies,
        average_rating=average_rating,
    )
