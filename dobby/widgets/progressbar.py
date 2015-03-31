from __future__ import print_function, absolute_import, division

from ..libs import *
from .base import Widget

class ProgressBar(Widget):
    def __init__(self, max=None, value=None, style=NSProgressIndicatorBarStyle):
        super(ProgressBar, self).__init__()
        self.max = max
        self.style = style
        self.startup()
        self.value = value

    def startup(self):
        self._impl = NSProgressIndicator.new()
        self._impl.setStyle_(self.style)
        self._impl.setDisplayedWhenStopped_(False)
        if self.max:
            self._impl.setIndeterminate_(False)
            self._impl.setMaxValue_(self.max)
        else:
            self._impl.setIndeterminate_(True)

        self._impl.setUsesThreadedAnimation_(True)
        self._impl.setTranslatesAutoresizingMaskIntoConstraints_(False)

    def setStyleSpinner(self):
        self.style = NSProgressIndicatorSpinningStyle
        self._impl.setStyle_(self.style)

    def setStyleBar(self):
        self.style = NSProgressIndicatorBarStyle
        self._impl.setStyle_(NSProgressIndicatorBarStyle)

    def toggleStyle(self):
        if(self.style == NSProgressIndicatorBarStyle):
            self.setStyleSpinner()
        else:
            self.setStyleBar()

    def add(self, value):
        self._value = self._value + value
        self._impl.incrementBy_(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._running = self._value is not None
        if value is not None:
            self._impl.setDoubleValue_(value)

    def start(self):
        if self._impl and not self._running:
            self._impl.startAnimation_(self._impl)
            self._running = True

    def stop(self):
        if self._impl and self._running:
            self._impl.stopAnimation_(self._impl)
            self._running = False
