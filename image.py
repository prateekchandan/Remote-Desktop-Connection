import pyscreenshot as ImageGrab
im=ImageGrab.grab()
pixels = list(im.getdata())
width, height = im.size
#pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
print len(pixels)
print width,height

