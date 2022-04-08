from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select

from issue.application import interfaces
from issue.application.dataclasses import Issue


@component
class IssuesRepo(BaseRepository, interfaces.IssuesRepo):

    def add(self, issue: Issue):
        self.session.add(issue)
        self.session.flush()
        self.session.commit()

    def get_all_issues(self) -> Optional[Issue]:
        query = select(Issue)
        return self.session.execute(query).scalars().all()
