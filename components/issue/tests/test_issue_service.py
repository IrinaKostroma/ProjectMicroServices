from attr import asdict
from datetime import datetime

data = {
    'action': 'add_book',
    'created': datetime.now(),
    'book_id': 1,
    'user_id': None
}


def test_add_issue(service,issues_repo):
    service.add_issue(**data)
    service.issues_repo.add.assert_called_once()


def test_get_all_issues(service, issues_repo):
    assert service.get_all_issues() == issues_repo.get_all()
