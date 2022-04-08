import pytest


def test__add_book(service, book):
    data = {
        'title': 't1',
        'author': 'a1',
        'year': 1,
        'id': 1,
    }
    assert service.add_book(**data) is None
