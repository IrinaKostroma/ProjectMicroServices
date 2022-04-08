from unittest.mock import Mock
import pytest

from classic.messaging import Publisher


from book.application import dataclasses, interfaces
from book.application.services import BookService


@pytest.fixture
def book():
    return dataclasses.Book(
        title='title1',
        author='author1',
        year=1,
        id=1,
    )


@pytest.fixture(scope='function')
def books_repo(book):
    books_repo = Mock(interfaces.BooksRepo)
    books_repo.add_book = Mock(return_value=book)
    books_repo.get_book = Mock(return_value=book)
    books_repo.get_all_books = Mock(return_value=book)
    return books_repo


@pytest.fixture(scope='function')
def book_publisher():
    book_publisher = Mock(Publisher)
    book_publisher.plan = Mock(return_value=None)
    return book_publisher


@pytest.fixture(scope='function')
def service(books_repo, book_publisher):
    return BookService(
        books_repo=books_repo,
        publisher=book_publisher,
    )