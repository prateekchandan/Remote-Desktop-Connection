from pymouse import PyMouse
import sys

m = PyMouse()

def MouseClick(x,y,event):
	m.click(x, y, event)

def MouseGo(x,y):
	m.move(x,y)

arguments= sys.argv
arguments = [int(x) for x in arguments[1:]]

if len(arguments) == 1:
	pass
elif  arguments[0] == 0:
	MouseGo(arguments[1],arguments[2])
elif arguments[0] == 1:
	MouseClick(arguments[1],arguments[2],arguments[3])