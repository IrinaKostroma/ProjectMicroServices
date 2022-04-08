from classic.http_api import App

from issue.application import services

from .import controllers


def create_app(issues: services.IssueService) -> App:

    app = App(prefix='/api')

    app.register(controllers.Issues(issues=issues))

    return app

