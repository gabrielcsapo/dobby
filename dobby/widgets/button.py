from __future__ import print_function, absolute_import, division

from .base import Widget
from ..libs import *
from ..utils import process_callback

class ButtonImpl_impl(object):
    ButtonImpl = ObjCSubclass('NSButton', 'ButtonImpl')

    @ButtonImpl.method('v@')
    def onPress_(self, obj):
        if self.interface.on_click:
            process_callback(self.interface.on_click(self.interface))

ButtonImpl = ObjCClass('ButtonImpl')

class Button(Widget):
    def __init__(self, label, on_click=None, type=NSMomentaryPushInButton):
        super(Button, self).__init__()
        self.label = label
        self.type = type
        self.on_click = on_click
        self.startup()

    def startup(self):
        self._impl = ButtonImpl.alloc().init()
        self._impl.interface = self

        self._impl.setBezelStyle_(NSRoundedBezelStyle)
        self._impl.setButtonType_(self.type)
        self._impl.setTitle_(get_NSString(self.label))
        self._impl.setTarget_(self._impl)
        self._impl.setAction_(get_selector('onPress:'))
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    def setMomentaryButton(self):
        self._impl.setButtonType_(NSMomentaryLightButton)

    def setToggleButton(self):
        self._impl.setButtonType_(NSToggleButton)

    def setBasicButton(self):
        self._impl.setButtonType_(NSPushOnPushOffButton)

    def setSwitchButton(self):
        self._impl.setButtonType_(NSSwitchButton)

    def setRadioButton(self):
        self._impl.setButtonType_(NSRadioButton)
    
    def setMomentaryChangeButton(self):
        self._impl.setButtonType_(NSMomentaryChangeButton)

    def setOnOffButton(self):
        self._impl.setButtonType_(NSOnOffButton)

    def setMomentaryPushInButton(self):
        self._impl.setButtonType_(NSMomentaryPushInButton)

    def state(self):
        return cftype_to_value(self._impl.valueForKey_(get_NSString('state')))
        
        
