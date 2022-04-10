from classic.http_api import App

from issue.adapters.issue_api import controllers
from issue.application import services


def create_app(issues: services.IssueService) -> App:

    app = App(prefix='/api')

    app.register(controllers.Issues(issues=issues))

    return app

