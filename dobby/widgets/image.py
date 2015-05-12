from .widget import *

class Image(Widget):
    def __init__(self, path, height=None, width=None):
        super(Image, self).__init__()
        self.path = path
        self.height = height
        self.width = width
        self.startup()

    def startup(self):
        self._impl = NSImage.alloc().initWithContentsOfFile_(get_NSString(self.path))
        if(self.height and self.width):
            size = NSMakeSize(self.width, self.height)
            self._impl.setSize_(size)

    def get_image(self):
        return self._impl