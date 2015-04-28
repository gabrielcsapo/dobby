from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget
from ..utils import process_callback
from ..constants import *

class Label_impl(object):

    LabelImpl = ObjCSubclass('NSTextField', 'LabelImpl')

    @LabelImpl.method('v@')
    def mouseDown_(self, notification):
        if self.interface.on_click:
            process_callback(self.interface.on_click(self.interface))

    @LabelImpl.method('v@')
    def mouseDragged_(self, notification):
        if self.interface.on_mouse_drag:
            process_callback(self.interface.on_mouse_drag(self.interface))

    @LabelImpl.method('v@')
    def mouseUp_(self, notification):
        if self.interface.on_mouse_up:
            process_callback(self.interface.on_mouse_up(self.interface))

LabelImpl = ObjCClass('LabelImpl')

class Label(Widget):
    def __init__(self, text=None, alignment=LEFT_ALIGNED, on_click=None, on_mouse_drag=None, on_mouse_up=None):
        super(Label, self).__init__()

        self.text = text
        self.on_click = on_click
        self.on_mouse_drag = on_mouse_drag
        self.on_mouse_up = on_mouse_up

        self.startup()
        self.alignment = alignment

    def startup(self):
        self._impl = LabelImpl.alloc().init()
        self._impl.interface = self
        self._impl.setStringValue_(get_NSString(self.text))
        self._impl.setDrawsBackground_(False)
        self._impl.setEditable_(False)
        self._impl.setBezeled_(False)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self._impl.setTarget_(self._impl)

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, value):
        self._alignment = value
        self._impl.setAlignment_(NSTextAlignment(self._alignment))
