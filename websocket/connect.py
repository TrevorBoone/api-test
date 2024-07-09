import websockets, asyncio

async def send():
    url = 'ws://localhost:8765'
    async with websockets.connect(url) as websocket:
        while True:
            message = input("message: ")
            await websocket.send(message)
            print("received: " + await websocket.recv())
      
def run():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send())

run()