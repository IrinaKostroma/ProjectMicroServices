from typing import Tuple, Union

from classic.http_api import App

from book.application import services

from .import controllers


def create_app(books: services.BookService) -> App:

    app = App(prefix='/api')

    app.register(controllers.Books(books=books))

    return app
