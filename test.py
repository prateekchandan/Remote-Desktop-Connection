#!/usr/bin/env python

import asyncio
import websockets

@asyncio.coroutine
def hello(websocket, path):
	name="k"
	while name!="exit":
	    name = yield from websocket.recv()
	    print("< {}".format(name))
	    greeting = "Hello {}!".format(name)
	    yield from websocket.send(name)
	    yield from websocket.send(greeting)
	    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8882)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
