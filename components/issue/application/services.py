from typing import Optional, List
from datetime import datetime

from classic.components import component
from classic.aspects import PointCut
from classic.app import DTO
from pydantic import validate_arguments

from issue.application import interfaces
from .dataclasses import Issue


join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    action: str
    created: datetime
    user_id: Optional[int] = None
    book_id: Optional[int] = None
    id: Optional[int] = None


@component
class IssueService:
    issues_repo: interfaces.IssuesRepo

    @join_point
    @validate_arguments
    def add_issue(self,  action: str, created: datetime, book_id: int = None, user_id: int = None):
        issue_info = IssueInfo(action=action, created=created, book_id=book_id, user_id=user_id)
        issue = issue_info.create_obj(Issue)
        self.issues_repo.add(issue)

    @join_point
    @validate_arguments
    def get_all_issues(self) -> List[Issue]:
        issues = self.issues_repo.get_all()
        return issues
