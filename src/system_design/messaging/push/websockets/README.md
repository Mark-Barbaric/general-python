# Websocket

## Connect 4 using Websockets

### Start frontend and backend

In order to overcome CORS issues, you will need to start the frontend using the http.server python module as below:

>`python3 -m http.server 3000 -d src/system_design/messaging/push/connect_4/frontend`

Then in another terminal run the websocket server:

>`python3 websocket_client_server/main.py`