import asyncio
import websockets
import itertools
import json
from connect4 import Connect4, PLAYER1, PLAYER2


async def handler(websocket):
    try:
        game = Connect4()
        turns = itertools.cycle([PLAYER1, PLAYER2])
        cur_player = next(turns)

        async for message in websocket:
            print(f"websocket_sever - message - {message}")
            event = json.loads(message)
            assert event['type'] == 'play'
            column = event['column']

            try:
                row = game.play(cur_player, column)
            except RuntimeError as err:
                event = {
                    'type': 'error',
                    'message': str(err)
                }
                await websocket.send(json.dumps(event))
                continue

            event = {
                "type": "play",
                "player": cur_player,
                "column": column,
                "row": row,
            }
            await websocket.send(json.dumps(event))

            if game.winner is not None:
                event = {
                    "type": "win",
                    "player": game.winner,
                }
                await websocket.send(json.dumps(event))

            cur_player = next(turns)

    except websockets.ConnectionClosedError as err:
        print(f"websocket_server - connection failed with error - {err}")


async def websocket_server():
    async with websockets.serve(handler, 'localhost', 8000):
        await asyncio.Future()


if __name__ == '__main__':
    print("Starting websocker server")
    asyncio.run(websocket_server())
