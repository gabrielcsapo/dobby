from .widget import *

class MenuDelegate_(object):
    MenuDelegate = ObjCSubclass('NSMenu', 'MenuDelegate')

    @MenuDelegate.method("@@")
    def menuDidClose_(self, menu):
        if self.interface.on_close:
            process_callback(self.interface.on_close(self.interface))

    @MenuDelegate.method("@@")
    def menuWillOpen_(self, menu):
        if self.interface.on_open:
            process_callback(self.interface.on_open(self.interface))

    @MenuDelegate.method("@@")
    def itemChanged_(self, menu):
        if self.interface.on_open_first:
            process_callback(self.interface.on_open_first(self.interface))

    @MenuDelegate.method("v@")
    def sendAction_(self, obj):
        callback = self.interface._callbacks[obj]
        callback['function'](callback['text'])

MenuDelegate = ObjCClass('MenuDelegate')

class StatusBar(Widget):

    def __init__(self, title="", on_open=None, on_close=None, on_open_first=None):
        super(StatusBar, self).__init__()
        self.title = title
        self._callbacks = {}
        self.on_open = on_open
        self.on_close = on_close
        self.on_open_first = on_open_first
        self.startup()

    def startup(self):
        self._menu = MenuDelegate.alloc().initWithTitle_(get_NSString(self.title))
        self._menu.interface = self
        self._menu.setDelegate_(self._menu)
        self._menu.setAutoenablesItems_(True)
        self._menu.setMenuChangedMessagesEnabled_(True)
        self._impl = NSStatusBar.systemStatusBar()
        self._item = self._impl.statusItemWithLength_(NSVariableStatusItemLength)
        self._item.setMenu_(self._menu)
        self._item.setTitle_(get_NSString(self.title))
        self._item.setHighlightMode_(True)

    def add_item(self, text, function=None, tooltip=""):
        item = NSMenuItem.alloc()
        item.setTitle_(get_NSString(text))
        item.setEnabled_(True)
        item.setTarget_(self._menu)
        item.setAction_(get_selector('sendAction:'))
        item.setToolTip_(get_NSString(tooltip))
        self._callbacks[item] = dict(text=text,function=function)
        self._menu.addItem_(item)

    def add_seperator(self):
        item = NSMenuItem.alloc()
        self._menu.addItem_(item.separatorItem())

    def add_view(self, view):
        item = NSMenuItem.alloc()
        item.setEnabled_(True)
        item.setTarget_(item)
        item.setView_(view)
        self._menu.addItem_(item)