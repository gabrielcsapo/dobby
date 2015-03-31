# Core capabilities
from .app import *
from .window import *
from .command import *

# Widgets
from .widgets.button import *
from .widgets.container import *
from .widgets.dialog import *
from .widgets.icon import *
from .widgets.label import *
from .widgets.tabcontainer import *
from .widgets.passwordinput import *
from .widgets.progressbar import *
from .widgets.scrollcontainer import *
from .widgets.splitview import *
from .widgets.statusbar import *
from .widgets.tableview import *
from .widgets.textinput import *
from .widgets.textview import *
from .widgets.tree import *
from .widgets.webview import *

__all__ = [
    '__version__',
    'App',
    'Window',
    'Command', 'SEPARATOR', 'SPACER', 'EXPANDING_SPACER',
    'Button',
    'Container',
    'Icon',
    'Label',
    'Dialog',
    'TextView',
    'TabContainer',
    'PasswordInput',
    'ProgressBar',
    'ScrollContainer',
    'SplitView',
    'StatusBar',
    'TableView',
    'TextInput',
    'Tree',
    'WebView',
]

__version__ = '0.1'

import platform

if tuple(int(v) for v in platform.mac_ver()[0].split('.')[:2]) < (10, 7):
    raise RuntimeError('Dobby requires OS X 10.7 (Lion) or greater.')
