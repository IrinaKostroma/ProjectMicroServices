from classic.http_api import App

from user.application import services

from .import controllers


def create_app(users: services.UserService) -> App:

    app = App(prefix='/api')

    app.register(controllers.Users(users=users))

    return app
