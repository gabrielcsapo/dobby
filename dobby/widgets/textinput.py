from .widget import *

class TextInputDelegate_(object):
    TextInputDelegate = ObjCSubclass('NSTextField', 'TextInputDelegate')

    @TextInputDelegate.method('v@')
    def textDidChange_(self, notification):
        if self.interface.on_textChange:
            Widget.callback(self.interface.on_textChange())

    @TextInputDelegate.method('v@')
    def textDidBeginEditing_(self, notification):
        if self.interface.on_beginEditing:
            Widget.callback(self.interface.on_beginEditing())

    @TextInputDelegate.method('v@')
    def textDidEndEditing_(self, notification):
        if self.interface.on_endEditing:
            Widget.callback(self.interface.on_endEditing())

    @TextInputDelegate.method('v@')
    def keyUp_(self, event):
        if self.interface.on_keyUp:
            keyCode = cftype_to_value(event.valueForKey_(get_NSString('keyCode')))
            Widget.callback(self.interface.on_keyUp(keyCode))

    @TextInputDelegate.method('v@')
    def keyDown_(self, event):
        keyCode = cftype_to_value(event.valueForKey_(get_NSString('keyCode')))

class SecureTextInputDelegate_(object):
    SecureTextInputDelegate = ObjCSubclass('NSSecureTextField', 'SecureTextInputDelegate')

    @SecureTextInputDelegate.method('v@')
    def textDidChange_(self, notification):
        if self.interface.on_textChange:
            Widget.callback(self.interface.on_textChange())

    @SecureTextInputDelegate.method('v@')
    def textDidBeginEditing_(self, notification):
        if self.interface.on_beginEditing:
            Widget.callback(self.interface.on_beginEditing())

    @SecureTextInputDelegate.method('v@')
    def textDidEndEditing_(self, notification):
        if self.interface.on_endEditing:
            Widget.callback(self.interface.on_endEditing())

SecureTextInputDelegate = ObjCClass('SecureTextInputDelegate')
TextInputDelegate = ObjCClass('TextInputDelegate')

class TextInput(Widget):

    def __init__(self, initial=None, placeholder=None, readonly=False, on_keyUp=None, on_endEditing=None, on_beginEditing=None, on_textChange=None, secure=False):
        super(TextInput, self).__init__()

        self.secure = secure
        self.startup()
        self.readonly = readonly
        self.placeholder = placeholder
        self.value = initial
        
        self.on_keyUp = on_keyUp
        self.on_endEditing = on_endEditing
        self.on_beginEditing = on_beginEditing
        self.on_textChange = on_textChange

    def startup(self):
        if not(self.secure):
            self._impl = TextInputDelegate.alloc().init()
        else:
            self._impl = SecureTextInputDelegate.alloc().init()

        self._impl.interface = self
        self._impl.setBezeled_(True)
        self._impl.setBezelStyle_(NSTextFieldSquareBezel)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)
        self._impl.setTarget_(self._impl)

    @property
    def readonly(self):
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        self._readonly = value
        self._impl.setEditable_(not self._readonly)

    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value):
        self._placeholder = value
        if value:
            self._impl.cell.setPlaceholderString_(get_NSString(self.placeholder))

    @property
    def value(self):
        return cfstring_to_string(self._impl.stringValue())

    @value.setter
    def value(self, value):
        if value:
            self._impl.setStringValue_(get_NSString(text(value)))