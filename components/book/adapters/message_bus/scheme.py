from kombu import Exchange, Queue

from classic.messaging_kombu import BrokerScheme

broker_scheme = BrokerScheme(
    Queue('log', Exchange('log'))
)