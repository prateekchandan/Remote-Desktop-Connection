from pymouse import PyMouse
import sys
import gtk

m = PyMouse()

def MouseClick(x,y,event):
	if event>0:
		m.press(x, y, event)
	else:
		m.release(x,y,abs(event))

def MouseGo(x,y):
	m.move(x,y)

arguments= sys.argv
arguments = [int(float(x)) for x in arguments[1:]]


width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()


if len(arguments) == 0:
	pass
elif  arguments[0] == 0:
	arguments[1] = int((arguments[1] * width)/1000.0)
	arguments[2] = int((arguments[2] * height)/1000.0)
	MouseGo(arguments[1],arguments[2])
elif arguments[0] == 1:
	arguments[1] = (arguments[1] * width)/1000
	arguments[2] = (arguments[2] * height)/1000
	MouseClick(arguments[1],arguments[2],arguments[3])