from .icon import Icon
from ..libs import *

class Dialog(object):

    @staticmethod
    def alert(title, message, style=NSInformationalAlertStyle):
        alert = NSAlert.alloc().init()
        alert.icon = Icon.app_icon._impl
        alert.setAlertStyle_(style)
        alert.setMessageText_(get_NSString(title))
        alert.setInformativeText_(get_NSString(message))
        return alert

    @staticmethod
    def info(title, message):
        alert = Dialog.alert(title, message)
        alert.runModal()

    @staticmethod
    def choice(title, message, choice=[]):
        alert = Dialog.alert(title, message)

        for x in choice:
            alert.addButtonWithTitle_(get_NSString(x))

        result = alert.runModal()
        return result - 1000

    @staticmethod
    def question(title, message):
        alert = Dialog.alert(title, message)

        alert.addButtonWithTitle_(get_NSString('Yes'))
        alert.addButtonWithTitle_(get_NSString('No'))

        result = alert.runModal()
        return result == NSAlertFirstButtonReturn

    @staticmethod
    def confirm(title, message):

        alert = Dialog.alert(title, message, style=NSWarningAlertStyle)

        alert.addButtonWithTitle_(get_NSString('OK'))
        alert.addButtonWithTitle_(get_NSString('Cancel'))

        result = alert.runModal()
        return result == NSAlertFirstButtonReturn

    @staticmethod
    def error(title, message):
        alert = Dialog.alert(title, message, style=NSCriticalAlertStyle)
        alert.runModal()

    @staticmethod
    def stack_trace(title, message, content, retry=False):
        alert = Dialog.alert(title, message, style=NSCriticalAlertStyle)

        scroll = NSScrollView.alloc().initWithFrame_(NSMakeRect(0,0,350,200))
        scroll.setHasVerticalScroller_(True)
        scroll.setHasHorizontalScroller_(False)
        scroll.setAutohidesScrollers_(False)
        scroll.setBorderType_(NSBezelBorder)

        trace = NSTextView.alloc().init()
        trace.insertText_(get_NSString(content))
        trace.setEditable_(False)
        trace.setVerticallyResizable_(True)
        trace.setHorizontallyResizable_(True)

        scroll.setDocumentView_(trace)
        alert.setAccessoryView_(scroll)

        if retry:
            alert.addButtonWithTitle_(get_NSString('Retry'))
            alert.addButtonWithTitle_(get_NSString('Cancel'))
            result = alert.runModal()
            return result == NSAlertFirstButtonReturn
        else:
            alert.runModal()
