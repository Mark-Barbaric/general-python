from pika import BlockingConnection, ConnectionParameters
from subscriber import Subscriber
from queue_params import exchange_name, binding_key
import sys


if __name__ == '__main__':

    print("main")
    connection_config = {
        'host': 'localhost',
        'port': 5671
    }
    connection = None
    try:
        connection = BlockingConnection(ConnectionParameters('localhost'))
        print("Successfully established connection")
    except RuntimeError:
        print("Failed to establish connection to RabbitMQ. Exiting")
        sys.exit()

    subscriber_channel1 = connection.channel()
    subscriber1 = Subscriber(
        channel=subscriber_channel1,
        exchange=exchange_name,
        queue_name='subscriber_1',
        binding_key=binding_key
        )
    subscriber1.setup()
