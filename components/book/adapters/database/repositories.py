from typing import Optional, List

from sqlalchemy import select

from classic.components import component
from classic.sql_storage import BaseRepository

from book.application import interfaces
from book.application.dataclasses import Book


@component
class BooksRepo(BaseRepository, interfaces.BooksRepo):

    def get_by_id(self, id_: int) -> Optional[Book]:
        query = select(Book).where(Book.id == id_)
        return self.session.execute(query).scalars().one_or_none()

    def get_all_books(self) -> List[Book]:
        query = select(Book)  # .order_by(Book.id)
        return self.session.execute(query).scalars().all()

    def add(self, book: Book):
        self.session.add(book)
        self.session.flush()
        self.session.commit()

    def get_or_create(self, id_: Optional[int]) -> Book:
        if id_ is None:
            book = Book()
            self.add(book)
        else:
            book = self.get_by_id(id_)
            if book is None:
                book = Book()
                self.add(book)
        return book
