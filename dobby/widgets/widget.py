from __future__ import print_function, absolute_import, division
from ..utils import Attribute
from ..libs import *
from ..constants import *
import inspect

class Widget(object):
    def __init__(self):
        self._window = None
        self._app = None
        self._impl = None

        self.LEFT = Attribute(self, Attribute.LEFT)
        self.RIGHT = Attribute(self, Attribute.RIGHT)
        self.TOP = Attribute(self, Attribute.TOP)
        self.BOTTOM = Attribute(self, Attribute.BOTTOM)
        self.LEADING = Attribute(self, Attribute.LEADING)
        self.TRAILING = Attribute(self, Attribute.TRAILING)
        self.WIDTH = Attribute(self, Attribute.WIDTH)
        self.HEIGHT = Attribute(self, Attribute.HEIGHT)
        self.CENTER_X = Attribute(self, Attribute.CENTER_X)
        self.CENTER_Y = Attribute(self, Attribute.CENTER_Y)

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, app):
        if self._app:
            raise Exception("Widget %r is already associated with an App" % self)
        self._app = app
        self._set_app(app)

    def _set_app(self, app):
        pass

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, window):
        self._window = window
        self._set_window(window)

    def _set_window(self, window):
        pass

    def __repr__(self):
        return "<%s:%s>" % (self.__class__.__name__, id(self))

    def startup(self):
        pass

    def get_inst(self):
        return self._impl

    @staticmethod
    def callback(callback_result):
        if inspect.isgenerator(callback_result):
            task = LongRunningTask.alloc().init()
            task.interface = callback_result