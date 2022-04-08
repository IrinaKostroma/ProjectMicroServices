import pytest

from book.application.services import BookService


@pytest.fixture(scope='function')
def service(books_repo, book_publisher):
    return BookService(
        books_repo=books_repo,
        publisher=book_publisher,
    )


def test__add_book(service, book):
    data = {
        'title': 't1',
        'author': 'a1',
        'year': 1,
        'id': 1,
    }
    assert service.add_book(**data) is None
