from unittest.mock import Mock

import pytest

from classic.messaging import Publisher

from book.application import interfaces


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
