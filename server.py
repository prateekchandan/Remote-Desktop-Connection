#!/usr/bin/env python

import asyncio
import websockets
import os
import threading
import time
import sys
import getpass
import subprocess

width,height =[int(a) for a in str(subprocess.check_output("xrandr | grep '*' | awk '{print $1}'", shell=True))[2:-3].split('x')]


testing = 0 # repalce by 1 for testing


def control_events(msg):
	try:
		keys,mouse,pointer = msg.split('|')
		key_events = keys.split(',')

		for event in key_events:
			if event != "":
				os.system("python keypress.py " + event + " > log" )

		m_events = mouse.split(',')
		for event in m_events:
			if event != "":
				x,y,e=[int(float(a)) for a in event.split(' ')]
				x=str((x*width)/1000.0)
				y=str((y*height)/1000.0)
				e1=str(abs(e))
				if e > 0:
					os.system("xdotool mousemove "+x+" "+y+" mousedown "+e1)
					#os.system("python mouse.py 1 "+x+" "+y+" "+e+ " > log" )
				else:
					os.system("xdotool mousemove "+x+" "+y+" mouseup "+e1)
		
		x,y=[int(float(a)) for a in pointer.split(',')]
		x=str((x*width)/1000.0)
		y=str((y*height)/1000.0)
		if not testing:
			os.system("xdotool mousemove "+x+" "+y)
			#os.system("python mouse.py 0 "+x+" "+y+ " > log")
	except ValueError:
		pass


def key_control_events(msg):
		key_events = msg.split(',')

		for event in key_events:
			if event != "":
				os.system("python keypress.py " + event + " > log" )


def mouse_control_events(msg):
		m_events = msg.split(',')
		for event in m_events:
			if event != "":
				x,y,e=[int(float(a)) for a in event.split(' ')]
				x=str((x*width)/1000.0)
				y=str((y*height)/1000.0)
				e1=str(abs(e))
				if e > 0:
					os.system("xdotool mousemove "+x+" "+y+" mousedown "+e1)
					#os.system("python mouse.py 1 "+x+" "+y+" "+e+ " > log" )
				else:
					os.system("xdotool mousemove "+x+" "+y+" mouseup "+e1)


def pointer_control_events(msg):
		x,y=[int(float(a)) for a in msg.split(',')]
		x=str((x*width)/1000.0)
		y=str((y*height)/1000.0)
		if not testing:
			os.system("xdotool mousemove "+x+" "+y)
			#os.system("python mouse.py 0 "+x+" "+y+ " > log")


pwd="default"


class AsyncEvent(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.event_list = []

	def run(self):
		while 1:
			if len(self.event_list) != 0:
				control_events(self.event_list.pop(0))


class AsyncEvent_key(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.event_list = []

	def run(self):
		while 1:
			if len(self.event_list) != 0:
				key_control_events(self.event_list.pop(0))

class AsyncEvent_mouse(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.event_list = []

	def run(self):
		while 1:
			if len(self.event_list) != 0:
				mouse_control_events(self.event_list.pop(0))

class AsyncEvent_pointer(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.event_list = []

	def run(self):
		while 1:
			if len(self.event_list) != 0:
				pointer_control_events(self.event_list.pop(0))



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

	background = AsyncEvent()
	background.start()
	
	background_key = AsyncEvent_key()
	background_key.start()
	
	background_mouse = AsyncEvent_mouse()
	background_mouse.start()
	
	background_pointer = AsyncEvent_pointer()
	background_pointer.start()
	
	
	
	while 1:
		inp = yield from websocket.recv()
		if(inp=="exit"):
			break
		
		keys,mouse,pointer = inp.split('|')
		background_key.event_list.append(keys)
		background_mouse.event_list.append(mouse)
		background_pointer.event_list.append(pointer)
		
		#background.event_list.append(inp)
		#control_events(inp)
		os.system("python image_generator.py >log 2>&1")	
		f = open("temp.jpg", "rb")
		greeting = f.read()
		print(sys.getsizeof(greeting))
		#print(greeting)
		#f=open("out",'r')
		#greeting=f.read()
		#print("Sent : "+str(len(greeting))+" bytes")
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
