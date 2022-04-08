from classic.components import component

from .join_points import join_point

from issue.application import services


@component
class Issues:
    issues: services.IssueService

    @join_point
    def on_get_all_issues(self, request, response):
        issues = self.issues.get_all_issues()
        response.media = {
            'issue': str(issues),
        }
