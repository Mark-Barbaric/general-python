from pika import channel


class Subscriber:
    def __init__(self, channel: channel, exchange: str, queue_name: str, binding_key: str, exchange_type='topic'):
        self._channel = channel
        self._exchange = exchange
        self._queue_name = queue_name
        self._binding_key = binding_key
        self._exchange_type= exchange_type

    def on_message(self, channel, method, properties, body):
        binding_key = method.routing_key
        print(f"received new message on channel {channel} for {binding_key}")
        print(f"message_body: {body}")

    def setup(self):
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type=self._exchange_type
            )
        self._channel.queue_declare(
            queue=self._queue_name
            )
        self._channel.queue_bind(
            queue=self._queue_name,
            exchange=self._exchange,
            routing_key=self._binding_key
            )
        self._channel.basic_consume(
            queue=self._queue_name,
            on_message_callback=self.on_message,
            auto_ack=True)
        try:
            self._channel.start_consuming()
            print(f"Subscriber: {self._queue_name} consuming")
        except:
            print("Error")
        