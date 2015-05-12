from .widget import *

class ButtonDelegate_(object):
    ButtonDelegate = ObjCSubclass('NSButton', 'ButtonDelegate')

    @ButtonDelegate.method('v@')
    def onPress_(self, obj):
        if self.interface.on_click:
            Widget.callback(self.interface.on_click(self.interface))

ButtonDelegate = ObjCClass('ButtonDelegate')

class Button(Widget):
    def __init__(self, label, on_click=None, type=NSMomentaryPushInButton, image=None):
        super(Button, self).__init__()

        self.label = label
        self.type  = type
        self.image = image

        self.on_click = on_click
        self.startup()

    def startup(self):
        self._impl = ButtonDelegate.alloc().init()
        self._impl.interface = self

        self._impl.setBezelStyle_(NSRoundedBezelStyle)
        self._impl.setButtonType_(self.type)
        self._impl.setTitle_(get_NSString(self.label))
        self._impl.setTarget_(self._impl)
        self._impl.setAction_(get_selector('onPress:'))
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

        if(self.image):
            self._impl.setImage_(self.image)

    # :Style
    # NSMomentaryLightButton
    # NSToggleButton
    # NSPushOnPushOffButton
    # NSSwitchButton
    # NSRadioButton
    # NSMomentaryChangeButton
    # NSOnOffButton
    # NSMomentaryPushInButton

    def set_style(self, _style):
        if(_style == 'NSMomentaryLightButton'): {
            self._impl.setButtonType_(NSMomentaryLightButton)
        }
        elif(_style == 'NSToggleButton'): {
            self._impl.setButtonType_(NSToggleButton)
        }
        elif(_style == 'NSPushOnPushOffButton'): {
            self._impl.setButtonType_(NSPushOnPushOffButton)
        }
        elif(_style == 'NSSwitchButton'): {
            self._impl.setButtonType_(NSSwitchButton)
        }
        elif(_style == 'NSRadioButton'): {
            self._impl.setButtonType_(NSRadioButton)
        }
        elif(_style == 'NSMomentaryChangeButton'): {
            self._impl.setButtonType_(NSMomentaryChangeButton)
        }
        elif(_style == 'NSOnOffButton'): {
            self._impl.setButtonType_(NSOnOffButton)
        }
        elif(_style == 'NSMomentaryPushInButton'): {
            self._impl.setButtonType_(NSMomentaryPushInButton)
        }

    def state(self):
        return cftype_to_value(self._impl.valueForKey_(get_NSString('state')))
        
        
