from pika import BlockingConnection, ConnectionParameters
from publisher import Publisher
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
    except:
        print(f"Failed to establish connection to RabbitMQ. Exiting")
        sys.exit()
    
    publisher = Publisher(connection)
    publisher.publish('my_exchange', 'nse.nify', 'data')