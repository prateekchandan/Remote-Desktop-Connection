#!/usr/bin/env python

import asyncio
import websockets
#import thread

#@asyncio.coroutine
def hello(websocket, path):
	name="k"
	while name!="exit":
		name = yield from websocket.recv()
		try:
			r,g,b=name.split(",") 
			r=int(r)
			g=int(g)
			b=int(b)
		except ValueError:
			r=0
			g=0
			b=0
		else:
			pass

		greeting="["
		print(r)
		x=r
		if 1==1:
			y=1
			while y<=300:
				if y!=1:
					greeting+=","
				greeting+="["+str(r)+","+str(y)+","+str(r)+","+str(g)+","+str(b)+"]"
				y+=1
			x+=1
			

		greeting+="]"
		yield from websocket.send(greeting)
		print("image sent")

start_server = websockets.serve(hello, '', 7861)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
