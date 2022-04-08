from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from issue.application import services
from .scheme import broker_scheme


def create_consumer(
    connection: Connection, issues: services.IssueService
) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        issues.add_issue,
        'log',
    )
    return consumer
