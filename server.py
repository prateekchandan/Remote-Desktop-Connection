#!/usr/bin/env python

import asyncio
import websockets
import os
import threading
import time


def control_evets(msg):
	try:
		keys,mouse,pointer = msg.split('|')
		m_events = mouse.split(',')
		
		for event in m_events:
			if event != "":
				x,y,e=event.split(' ')
				os.system("python mouse.py 1 "+x+" "+y+" "+e)
		x,y=pointer.split(',')
		os.system("python mouse.py 0 "+x+" "+y)
	except ValueError:
		pass

@asyncio.coroutine
def hello(websocket, path):
	name="k"
	while name!="exit":
		name = yield from websocket.recv()
		control_evets(name)
		os.system("python testsc.py > out")
		f=open("out",'r')
		greeting=f.read()
		yield from websocket.send(greeting)
		#print(name)

start_server = websockets.serve(hello, '', 7861)
i=0

def take_screenshot():
	while 1:
		os.system("import -window root screen.bmp")
		time.sleep(0.01)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
