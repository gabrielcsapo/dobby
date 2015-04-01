from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget
from ..utils import process_callback
from ..constants import *

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