from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from user.adapters import database, user_api, message_bus
from user.adapters.database import repositories
from user.application import services


class Settings:
    db = database.Settings()
    user_api = user_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = repositories.UsersRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:
    user_service = services.UserService(users_repo=DB.users_repo,
                                        publisher=MessageBus.publisher)


class Aspects:
    services.join_points.join(DB.context)
    user_api.join_points.join(MessageBus.publisher, DB.context)


app = user_api.create_app(users=Application.user_service)

# with make_server('', 8000, app) as httpd:
#     print(f'Server running on http://localhost:{httpd.server_port} ...')
#     httpd.serve_forever()
