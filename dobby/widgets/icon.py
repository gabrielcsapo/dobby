from __future__ import print_function, absolute_import, division
from ..libs import *
from ..widgets.image import *
import dobby, os

class Icon(object):
    app_icon = None

    def __init__(self, path, system=False):
        self.path = path
        self.system = system

        if self.system:
            filename = os.path.join(os.path.dirname(dobby.__file__), 'resources', self.path)
            print(filename)
        else:
            filename = self.path

        self._impl = Image(filename).get_inst()

    @staticmethod
    def load(path_or_icon, default=None):
        if path_or_icon:
            if isinstance(path_or_icon, Icon):
                obj = path_or_icon
            else:
                obj = Icon(path_or_icon)
        elif default:
            obj = default
        return obj


DOBBY_ICON = Icon('dobby.icns', system=True)
