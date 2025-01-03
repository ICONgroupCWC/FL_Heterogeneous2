#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    uri = "ws://85.131.117.229:5000"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())