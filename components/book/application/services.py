from typing import Optional, List
from datetime import datetime

from pydantic import validate_arguments

from classic.components import component
from classic.aspects import PointCut
from classic.app import DTO
from classic.messaging import Message, Publisher

from .import interfaces
from .dataclasses import Book
from .errors import NoBook


join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    id: Optional[int]
    title: str = None
    author: str = None
    year: int = None


@component
class BookService:
    books_repo: interfaces.BooksRepo
    publisher: Publisher

    @join_point
    @validate_arguments
    def add_book(self, book_info: BookInfo) -> Book:
        book = book_info.create_obj(Book)
        self.books_repo.add(book)

        if self.publisher:
            self.publisher.plan(
                Message('log', {'action': 'add_book',
                                'user_id': None,
                                'book_id': book.id,
                                'data': datetime.now()
                                })
            )
        return book

    @join_point
    @validate_arguments
    def get_book(self, book_id: int) -> Book:
        book = self.books_repo.get_by_id(book_id)
        if book is None:
            raise NoBook(number=book_id)
        return book

    @join_point
    @validate_arguments
    def get_all_books(self) -> List[Book]:
        books = self.books_repo.get_all_books()
        return books
