import Image, gtk
import base64
import sys
from array import array
class screenshot:
    def __init__(self):
        self.img_width = gtk.gdk.screen_width()
        self.img_height = gtk.gdk.screen_height()

        self.screengrab = gtk.gdk.Pixbuf(
            gtk.gdk.COLORSPACE_RGB,
            False,
            8,
            self.img_width,
            self.img_height)

    def take(self):
        self.screengrab.get_from_drawable(
            gtk.gdk.get_default_root_window(),
            gtk.gdk.colormap_get_system(),
            0, 0, 0, 0,
            self.img_width,
            self.img_height)

        final_screengrab = Image.frombuffer(
          "RGB",
          (self.img_width, self.img_height),
          self.screengrab.get_pixels(),
          "raw",
          "RGB",
          self.screengrab.get_rowstride(),
          1)
        return final_screengrab

if __name__ == '__main__':
    import time
    screenshot = screenshot()
    im = screenshot.take()
    im.save("temp.jpg", "JPEG")
    """f = open("temp.jpg", "rb")
    bytes = bytearray(f.read())
    print sys.getsizeof(bytes)
    stri = base64.b64encode(bytes)
    print sys.getsizeof(stri)"""
