from classic.components import component

from .join_points import join_point

from issue.application import services


@component
class Issues:
    issues: services.IssueService

    @join_point
    def on_get_all_issues(self, request, response):
        issues = self.issues.get_all_issues()
        response.media = [
            {
                'action': issue.action,
                'user_id': issue.user_id,
                'book_id': issue.book_id,
            } for issue in issues
        ]
