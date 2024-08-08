import pika


class Publisher:
    def __init__(self, connection: pika.BlockingConnection):
        self._connection = connection

    def publish(self, exchange: str, routing_key: str, message: str):
        channel = self._connection.channel(1)
        channel.exchange_declare(exchange=exchange, exchange_type='topic')
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=message
        )
        print(f"Sent message {message} for {routing_key}")
        
        