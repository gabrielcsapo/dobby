from .textinput import TextInput

class PasswordInput(TextInput):

    def __init__(self, initial=None, placeholder=None, readonly=False, on_keyUp=None, on_endEditing=None, on_beginEditing=None, on_textChange=None):
        super(PasswordInput, self).__init__(initial, placeholder, readonly, on_keyUp, on_endEditing, on_beginEditing, on_textChange, secure=True)