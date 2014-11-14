import Image
import base64
from array import array
import pyscreenshot as ImageGrab

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

im=ImageGrab.grab()
im.save("temp.jpg", "JPEG")
f = open("temp.jpg", "rb")
bytes = bytearray(f.read())
#pBits = im.convert("RGBA").tostring("raw", "RGBA")
#data = im.load()
#bytes = bytearray(pBits)
stri = base64.b64encode(bytes)
print stri
