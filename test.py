#!/usr/bin/env python

import asyncio
import websockets
#import thread

#@asyncio.coroutine
def hello(websocket, path):
	name="k"
	while name!="exit":
	    name = yield from websocket.recv()
	    r,g,b=name.split(",") 
	    greeting="["
	    x=1
	    while x<=300:
	    	y=1
	    	while y<=300:
	    		if y!=1 or x!=1:
	    			greeting+=","
	    		greeting+="["+str(x)+","+str(y)+","+str(x)+","+str(0)+","+str(0)+"]"
	    		y+=1
	    	x+=1
	    	

	    greeting+="]"
	    yield from websocket.send(greeting)
	    print("sent an iamge")

start_server = websockets.serve(hello, 'localhost', 8881)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
