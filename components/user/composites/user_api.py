from wsgiref.simple_server import make_server

from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from user.application.services import UserService
from user.adapters import database, user_api, message_bus


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()
    user_api = user_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:

    user_service = UserService(users_repo=DB.users_repo,
                               publisher=MessageBus.publisher)

    is_dev_mode = Settings.user_api.IS_DEV_MODE
    allow_origins = Settings.user_api.ALLOW_ORIGINS


# class Aspects:
#     services.join_points.join(DB.context)
#     user_api.join_points.join(DB.context)


app = user_api.create_app(
    users=Application.user_service,
)

# with make_server('', 8000, app) as httpd:
#     print(f'Server running on http://localhost:{httpd.server_port} ...')
#     httpd.serve_forever()
