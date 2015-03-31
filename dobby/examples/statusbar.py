#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):
        self.dialog = dobby.Dialog()
        self.statusbar = dobby.StatusBar(title="Tasks")
        self.statusbar.addItem("toggleWindow", self.toggleWindow, "toggleWindow")
        self.statusbar.addItem("alert", self.alert, 'alert something')

    def toggleWindow(self, item):
        self.toggle()

    def alert(self, item):
        self.dialog.info("Info", "This product is fully native")

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()