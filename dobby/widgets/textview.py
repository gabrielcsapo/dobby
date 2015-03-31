from __future__ import print_function, absolute_import, division

from ..libs import get_NSString, NSTextView, NSScrollView, NSBezelBorder
from .base import Widget

class TextView(Widget):

    def __init__(self, initial=None):
        super(TextView, self).__init__()
        self.initial = initial

        self._text = None

        self.startup()

    def startup(self):
        # Create a multiline view, and put it in a scroll view.
        # The scroll view is the _impl, because it's the outer container.
        self._impl = NSScrollView.alloc().init()
        self._impl.setHasVerticalScroller_(True)
        self._impl.setHasHorizontalScroller_(False)
        self._impl.setAutohidesScrollers_(False)
        self._impl.setBorderType_(NSBezelBorder)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

        self._text = NSTextView.alloc().init()

        if self.initial:
            self._text.insertText_(get_NSString(self.initial))

        self._text.setEditable_(True)
        self._text.setVerticallyResizable_(True)
        self._text.setHorizontallyResizable_(True)
        self._impl.setDocumentView_(self._text)

    ''' BOOL : True or False '''
    def backgroundColor(self):
        return self._text.backgroundColor

    def insertText(self, string):
        self._text.insertText_(string)

    def allowsUndo(self):
        return self._text.allowsUndo_()

    def allowsUndo(self, bool):
        self._text.allowsUndo_(bool)

    def setSelectable(self, bool):
        self._text.setSelectable_(bool)

    def setFieldEditor(self, bool):
        self._text.setFieldEditor_(bool)

    def setRichText(self, bool):
        self._text.setRichText_(bool)

    def setImportsGraphics(self, bool):
        self._text.setImportsGraphics_(bool)

    def importsGraphics(self):
        return self._text.importsGraphics

    def allowsImageEditing(self):
        return self._text.allowsImageEditing

    def setAllowsImageEditing(self, bool):
        self._text.setAllowsImageEditing_(bool)

    def setAutomaticQuoteSubstitutionEnabled(self, bool):
        self._text.setAutomaticQuoteSubstitutionEnabled_(bool)

    def toggleAutomaticQuoteSubstitution(self):
        self._text.toggleAutomaticQuoteSubstitution_()

    def setAutomaticLinkDetectionEnabled(self, bool):
        self._text.setAutomaticLinkDetectionEnabled_(bool)

    def toggleAutomaticLinkDetection(self):
        self._text.toggleAutomaticLinkDetection_()

    def displaysLinkToolTips(self):
        return self._text.displaysLinkToolTips

    def setDisplaysLinkToolTips(self, bool):
        self._text.setDisplaysLinkToolTips(bool)