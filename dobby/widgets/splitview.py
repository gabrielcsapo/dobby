from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget

class SplitView(Widget):

    HORIZONTAL = True
    VERTICAL = False

    def __init__(self, direction=VERTICAL):
        super(SplitView, self).__init__()
        self._impl = None
        self._content = None

        self.direction = direction

        self.startup()

    def startup(self):
        self._impl = NSSplitView.alloc().init()
        self._impl.setVertical_(self.direction)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if len(content) != 2:
            raise ValueError('SplitView content must be a 2-tuple')
        self._content = content

        self._content[0].window = self.window
        self._content[0].app = self.app
        self._impl.addSubview_(self._content[0]._impl)

        self._content[1].window = self.window
        self._content[1].app = self.app
        self._impl.addSubview_(self._content[1]._impl)

    def set_vertical(self):
        self.HORIZONTAL = False
        self.VERTICAL = True
        self._impl.setVertical_(True)

    def set_horizontal(self):
        self.HORIZONTAL = True
        self.VERTICAL = False
        self._impl.setVertical_(False)

    def toggle(self):
        if(self.HORIZONTAL):
            self.setVertical()
        else:
            self.setHorizontal()
