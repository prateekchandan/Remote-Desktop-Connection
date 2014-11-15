from pymouse import PyMouse
import sys

m = PyMouse()

def MouseClick(x,y,event):
	m.click(x, y, event)
	print "click at "+str(x)+" , "+str(y)

def MouseGo(x,y):
	m.move(x,y)

arguments= sys.argv
arguments = [int(x) for x in arguments[1:]]


if len(arguments) == 0:
	pass
elif  arguments[0] == 0:
	MouseGo(arguments[1],arguments[2])
elif arguments[0] == 1:
	MouseClick(arguments[1],arguments[2],arguments[3])