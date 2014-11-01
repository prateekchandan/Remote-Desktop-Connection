
import pyscreenshot as ImageGrab

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

im=ImageGrab.grab()
pixels = list(im.getdata())
width, height = im.size
i=0
st = "["
while i<height:
	j=0
	while j<width:
		if i!=0 or j!=0:
			st+= ','
		t=i*width+j
		st+='['+str(j)+','+str(i)+',"'+str(rgb_to_hex(pixels[t]))+'"]'
		#pixels[t]=a
		j+=1
	i+=1

print st+']'
#print pixels
'''
import os
import io
import Image
import base64
from array import array

def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

bytes = readimage("./sc1.png")

i = 0
bytearr = []
while i < len(bytes):
	bytearr.append(bytes[i])
	i+=1
print bytearr

'''