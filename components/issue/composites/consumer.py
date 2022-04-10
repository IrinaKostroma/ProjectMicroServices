from kombu import Connection
from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext

from issue.adapters import database, message_bus
from issue.application import services


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.IssuesRepo(context=context)


class Application:
    issues = services.IssueService(
        issues_repo=DB.issues_repo,
    )


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    consumer = message_bus.create_consumer(connection, Application.issues)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


if __name__ == '__main__':
    MessageBus.declare_scheme()
    MessageBus.consumer.run()
