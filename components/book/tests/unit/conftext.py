import pytest

from book.application import dataclasses


@pytest.fixture
def book():
    return dataclasses.Book(
        title='title1',
        author='author1',
        year=1,
        id=1,
    )
