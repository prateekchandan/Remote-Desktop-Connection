#!/usr/bin/env python

import asyncio
import websockets
import os
import threading
import time



@asyncio.coroutine
def hello(websocket, path):
	name="k"
	while name!="exit":
		name = yield from websocket.recv()
		
		os.system("python testsc.py > out")
		f=open("out",'r')
		greeting=f.read()
		yield from websocket.send(greeting)
		print("image sent")
#		print( greeting)

start_server = websockets.serve(hello, '', 7861)
i=0

def take_screenshot():
	while 1:
		os.system("import -window root screen.bmp")
		time.sleep(0.01)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
