import asyncio
import websockets


async def websocket_client():
    print("websocket_client starting")
    url = 'ws://127.0.0.1:8000'
    try:
        async with websockets.connect(url) as ws:
            await ws.send("data packet 1")
            await ws.send("data packet 2")

            while True:
                msg = await ws.recv()
                print(f"websocket_client: message received {msg}")
    except ConnectionRefusedError as err:
        print(f"websocket_client - connection refused with error: {err}")


if __name__ == '__main__':
    asyncio.run(websocket_client())
