#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):
        
        main_container = dobby.Container()
        app.main_window.content = main_container

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()