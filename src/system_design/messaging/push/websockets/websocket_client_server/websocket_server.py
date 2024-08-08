import asyncio
import websockets


async def handler(websocket, path):
    try:
        while True:
            data = await websocket.recv()
            print(f"websocket_server - message received - {data}")
            reply = f"Data received as: {data}"
            await websocket.send(reply)

    except websockets.ConnectionClosedError:
        print("Internal Server Error.")


async def websocket_server():
    async with websockets.serve(handler, 'localhost', 8000):
        await asyncio.Future()


if __name__ == '__main__':
    print("Starting websocket_server")
    asyncio.run(websocket_server())
