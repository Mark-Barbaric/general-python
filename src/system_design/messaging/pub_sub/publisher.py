from pika import channel


class Publisher:
    def __init__(self, channel: channel, exchange: str):
        self._channel = channel
        self._exchange = exchange

    def publish(self, routing_key: str, message: str):
        self._channel.exchange_declare(exchange=self._exchange, exchange_type='topic')
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=routing_key,
            body=message
        )
        print(f"Sent message {message} for {routing_key}")
