from wsgiref.simple_server import make_server

from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from issue.application.services import IssueService
from issue.adapters import database, issue_api, message_bus


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()
    issue_api = issue_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.IssuesRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:

    issue_service = IssueService(issues_repo=DB.issues_repo)

    is_dev_mode = Settings.issue_api.IS_DEV_MODE
    allow_origins = Settings.issue_api.ALLOW_ORIGINS


# class Aspects:
#     services.join_points.join(DB.context)
#     user_api.join_points.join(DB.context)


app = issue_api.create_app(
    issues=Application.issue_service,
)

# with make_server('', 8002, app) as httpd:
#     print(f'Server running on http://localhost:{httpd.server_port} ...')
#     httpd.serve_forever()
