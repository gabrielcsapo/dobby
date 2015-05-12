from __future__ import print_function, absolute_import, division
from .base import Widget
from ..libs import *

class View(Widget):

    def __init__(self):
        super(View, self).__init__()
        self.startup()

    def startup(self):
        self._impl = NSView.alloc().init()
    
    def add_view(self, view):
        self._impl.addSubview_(view)