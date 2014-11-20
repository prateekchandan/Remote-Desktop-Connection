REMOTE DESKTOP CONNECTION
================================
 
This is course project of Networks Lab CS378 . In this project we are creating a  program for browser based remote desktop connection to control a computer remotely from other computer

Note : run server on Python3.3 or Python3.4

Dependencies(Ubuntu/Linux Only) : 

1. **Python2.7** and **python3.3** or above (tested on Python3.3 and Python3.4)
2. **Web socket Library**. Go to Libraries/websockets do a
	sudo python3.4 setup.py build
	sudo python3.4 setup.py install
3. **xdotool** for mouse : 
	sudo apt-get install xdotool
4. **Pykeyboard** : sudo pip install pykeyboard
	Note : The library for this is include . To install
	goto Libraries/PyUserInput
	sudo python setup.py build
	sudo python setup.py install
5. **Xlib** : sudo apt-get install python-xlib (dependency for pykeyboard)
6. **pygtk** : To capture screens
	sudo pip install pygtk


Instructions to run Server :

1. python3.4 server.py
	You will be prompted for server password  which is required for clients to connect
2. Copy Client folder to your webhost location which is generally in /var/www/html
	now go to http://your_public_ip/client
	and enter password to connect

References:

1. **WebSockets Library** : [Checkout the Documentation](http://aaugustin.github.io/websockets/)
2. [Read about Threading in Python](https://docs.python.org/3.1/library/threading.html Python Docs)
3. [Notes on WebSockets by Aditya](https://docs.google.com/document/d/10Lrclx1eN2wRRM74Nwy_EV8Dc0Bq7MZn9TIpPG59Cuo/edit?usp=sharing Web Sockets)



[Get the Latest Working Code from Github](https://github.com/prateekchandan/Remote-Desktop-Connection "Github Link")

Team Members:

1. Prateek Chandan - 120050042
2. Aditya Kumar Akash - 120050046
3. Nishant Kumar Singh - 120050043
4. Anurag Shirolkar - 120050003

Guide :
Prof Varhsa Apte

Department Of Computer Science
IIT Bombay

