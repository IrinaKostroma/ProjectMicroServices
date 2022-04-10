from attr import asdict

data = {
    'title': 'title1',
    'author': 'author1',
    'user_id': None,
    'id': 1,
}

def test_add_book(service, books_repo):
    service.add_book(data)
    service.books_repo.add.assert_called_once()

def test_remove_book(service, books_repo):
    service.remove_book(id=1)
    service.books_repo.remove.assert_called_once()
