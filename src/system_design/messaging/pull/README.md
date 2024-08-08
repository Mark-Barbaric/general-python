# Pull Messaging

## Pub Sub Example

Uses RabbitMQ to demonstrate the pub sub messaging model.

### Setup

Need to have RabbitMQ server up and running prior. Use the below command in a terminal:

>`docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management`

In a new terminal run the main_subscribe script:

>`python main_subscribe.py`

Then run the main_publish script:

>`python main_publish.py`

You should see entries as below in the main_subscribe terminal:

message_body: b'data: 97'
received new message on channel <BlockingChannel impl=<Channel number=1 OPEN conn=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f357997c4f0> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>> for nse.nifty
message_body: b'data: 98'
received new message on channel <BlockingChannel impl=<Channel number=1 OPEN conn=<SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f357997c4f0> params=<ConnectionParameters host=localhost port=5672 virtual_host=/ ssl=False>>>> for nse.nifty
message_body: b'data: 99'