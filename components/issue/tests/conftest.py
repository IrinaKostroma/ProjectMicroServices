import pytest

from datetime import datetime
from unittest.mock import Mock

from issue.application import dataclasses, interfaces
from issue.application.services import IssueService

@pytest.fixture
def issue():
    return dataclasses.Issue(
        id=1,
        action='take_book',
        created=datetime.now(),
        book_id=1,
        user_id=1
    )


@pytest.fixture(scope='function')
def issues_repo(issue):
    issues_repo = Mock(interfaces.IssuesRepo)
    issues_repo.add_issue = Mock(return_value=None)
    issues_repo.get_all_issues = Mock(return_value=[issue, ])
    return issues_repo


@pytest.fixture(scope='function')
def service(issues_repo):
    return IssueService(
        issues_repo=issues_repo,
    )
