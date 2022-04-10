from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from book.adapters import database, book_api, message_bus
from book.adapters.database import repositories
from book.application import services


class Settings:
    db = database.Settings()
    book_api = book_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    books_repo = repositories.BooksRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:
    book_service = services.BookService(books_repo=DB.books_repo,
                                        publisher=MessageBus.publisher)


class Aspects:
    services.join_points.join(DB.context)
    book_api.join_points.join(MessageBus.publisher, DB.context)


app = book_api.create_app(books=Application.book_service)
