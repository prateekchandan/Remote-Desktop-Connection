#!/usr/bin/env python

import asyncio
import websockets
import os
import threading
import time
import sys
import getpass

testing = 0 # repalce by 1 for testing

def control_events(msg):
	try:
		keys,mouse,pointer = msg.split('|')
		key_events = keys.split(',')

		for event in key_events:
			if event != "":
				os.system("python keypress.py "+event+ ' > log' )
		m_events = mouse.split(',')
		for event in m_events:
			if event != "":
				x,y,e=event.split(' ')
				os.system("python mouse.py 1 "+x+" "+y+" "+e+ " > log" )

		
		x,y=pointer.split(',')
		if not testing:
			os.system("python mouse.py 0 "+x+" "+y+ " > log")

	except ValueError:
		pass

pwd="default"
@asyncio.coroutine
def client_handler(websocket, path):
	print("New connection established")
	while 1:
		inp = yield from websocket.recv()
		if(inp=="exit"):
			return
		if(inp==pwd):
			break
		yield from websocket.send("error")

	yield from websocket.send("connect")
	while 1:
		inp = yield from websocket.recv()
		if(inp=="exit"):
			break
		control_events(inp)
		os.system("python image_generator.py > out")
		f=open("out",'r')
		greeting=f.read()
		print("Sent : "+str(len(greeting))+" bytes")
		yield from websocket.send(greeting)

arg= sys.argv
if len(arg) > 1:
	testing=1

while 1:
	password = getpass.getpass("Enter server Password : ")
	repassword = getpass.getpass("Retype server Password : ")

	if(password==repassword):
		pwd=password
		break;

	print("Password mismatch")

print("Server started...")
start_server = websockets.serve(client_handler, '', 7862)

i=0

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
