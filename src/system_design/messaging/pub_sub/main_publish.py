from pika import BlockingConnection, ConnectionParameters
from publisher import Publisher
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

    publisher_channel = connection.channel()
    publisher = Publisher(channel=publisher_channel, exchange=exchange_name)

    for i in range(100):
        publisher.publish(binding_key, f'data: {i}')
