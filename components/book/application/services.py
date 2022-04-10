from typing import Optional, List
from datetime import datetime

from pydantic import validate_arguments

from classic.components import component
from classic.aspects import PointCut
from classic.app import DTO, validate_with_dto
from classic.messaging import Message, Publisher

from .import interfaces
from .dataclasses import Book
from .errors import NoBook, BookTaken


join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    id: Optional[int] = None
    title: str = None
    author: str = None
    user_id: Optional[int] = None


class BookInfoForChange(DTO):
    id: int
    title: Optional[str] = None
    author: Optional[str] = None
    user_id: Optional[int] = None


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
                                'created': datetime.now()
                                })
            )
        return book

    @join_point
    @validate_arguments
    def get_book(self, id: int) -> Book:
        book = self.books_repo.get_by_id(id)
        if book is None:
            raise NoBook(number=id)
        return book

    @join_point
    def get_all_books(self) -> List[Book]:
        books = self.books_repo.get_all()
        return books

    @join_point
    @validate_arguments
    def take_by_user(self, book_info: BookInfoForChange) -> Book:
        book = self.get_book(book_info.id)
        if book.user_id is not None:
            raise BookTaken(number=book.user_id)
        else:
            book_info.populate_obj(book)
            if self.publisher:
                self.publisher.plan(
                    Message('log', {'action': 'take_by_user',
                                    'user_id': book.user_id,
                                    'book_id': book.id,
                                    'created': datetime.now()
                                    })
                )

        return book

    @join_point
    @validate_arguments
    def return_book(self, book_info: BookInfoForChange) -> Book:
        book = self.get_book(book_info.id)
        book_info.user_id = None
        book_info.populate_obj(book)

        if self.publisher:
            self.publisher.plan(
                Message('log', {'action': 'return_book',
                                'user_id': None,
                                'book_id': book.id,
                                'created': datetime.now()
                                })
            )

        return book

    @join_point
    @validate_arguments
    def remove_book(self, id: int):
        book = self.get_book(id)
        self.books_repo.remove(book)
