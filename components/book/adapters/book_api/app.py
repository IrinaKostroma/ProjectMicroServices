from classic.http_api import App

from book.adapters.book_api import controllers
from book.application import services


def create_app(books: services.BookService) -> App:

    app = App(prefix='/api')

    app.register(controllers.Books(books=books))

    return app
