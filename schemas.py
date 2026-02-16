from datetime import date
from pydantic import BaseModel, ConfigDict


class AuthorDto(BaseModel):
    id: int | None = None
    name: str
    bio: str
    
    model_config = ConfigDict(from_attributes=True)


class AuthorListDto(AuthorDto):
    pass


class AuthorDetailDto(AuthorDto):
    books: list["BookDto"]


class BookDto(BaseModel):
    id: int | None = None
    title: str
    summary: str
    publication_date: date

    author_id: int
    
    model_config = ConfigDict(from_attributes=True)


class BookDetailDto(BookDto):
    author: AuthorDto
