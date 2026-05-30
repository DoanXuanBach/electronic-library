from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=120)
    authors: list[str] = Field(default_factory=list)
    description: str = Field(..., min_length=10, max_length=1200)
    publisher: str = Field(..., min_length=2, max_length=120)
    year: int = Field(..., ge=1000, le=2100)
    pages: int = Field(..., ge=1, le=10000)
    isbn: str = Field(..., min_length=5, max_length=30)
    language: str = Field(..., min_length=2, max_length=40)
    category: str = Field(..., min_length=2, max_length=60)
    cover_color: str = Field(default="#4f46e5", max_length=20)
    available_copies: int = Field(default=1, ge=0, le=100)
    rating: float = Field(default=4.5, ge=0, le=5)
    read_url: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int


class LibraryStats(BaseModel):
    total_books: int
    total_categories: int
    available_copies: int
    average_rating: float
