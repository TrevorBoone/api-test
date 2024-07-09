import asyncio
import websockets
import json

from .drawing import Drawing

drawing = Drawing()

async def echo(websocket):
    async for message in websocket:
        try:
            change = json.loads(message)
            drawing.change_pixel(change.x, change.y, change.color, change.user)
            await websocket.send(json.dumps({'change_id': change.id, 'outcome': "success"}))
        except Exception as err:
            await websocket.send(json.dumps({'change_id': change.id, 'outcome': "failure", 'error': err}))

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

print("yup")
asyncio.run(main())