from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget

'''Widget that allows multiple view panes'''
class TabContainer(Widget):
    def __init__(self):
        super(TabContainer, self).__init__()
        self._content = []

        self.startup()

    def startup(self):
        self._impl = NSTabView.alloc().init()
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    ''' Label: String'''
    ''' Container: Container'''
    def add(self, label, container):

        container.app = self.app
        container._impl.setTranslatesAutoresizingMaskIntoConstraints_(True)
        container.window = self.window

        self._content.append((label, container))

        item = NSTabViewItem.alloc().initWithIdentifier_(get_NSString('%s-Tab-%s' % (id(self), id(container))))
        item.setLabel_(get_NSString(label))
        item.setView_(container._impl)

        self._impl.addTabViewItem_(item)

    def numberOfTabViewItems(self):
        return self._impl.numberOfTabViewItems_()

    def selectFirstTabViewItem(self):
        self._impl.selectFirstTabViewItem_(self._impl)

    def selectLastTabViewItem(self):
        self._impl.selectLastTabViewItem_(self._impl)

    def selectNextTabViewItem(self):
        self._impl.selectNextTabViewItem_(self._impl)

    def selectPreviousTabViewItem(self):
        self._impl.selectPreviousTabViewItem_(self._impl)

    def selectTabViewItemAtIndex(self, index):
        self._impl.selectTabViewItemAtIndex_(index)
