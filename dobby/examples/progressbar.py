#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):

        main_container = dobby.Container()
        main_change_style = dobby.Button("Toggle Style", on_click=self.toggleStyle)
        main_container.add(main_change_style)
        main_container.constrain(main_change_style.TOP == main_container.TOP + 5)
        main_container.constrain(main_change_style.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(main_change_style.LEFT == main_container.LEFT + 5)

        main_increment = dobby.Button("+", on_click=self.add)
        main_container.add(main_increment)
        main_container.constrain(main_increment.TOP == main_change_style.BOTTOM + 15)
        main_container.constrain(main_increment.RIGHT == main_change_style.RIGHT - 5)
        main_container.constrain(main_increment.LEFT == main_change_style.LEFT + 5)

        self.main_progress = dobby.ProgressBar(max=50, value=0)
        self.main_progress.setStyleSpinner()

        main_container.add(self.main_progress)
        main_container.constrain(self.main_progress.BOTTOM == main_container.BOTTOM + 5)
        main_container.constrain(self.main_progress.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(self.main_progress.LEFT == main_container.LEFT + 5)

        app.main_window.content = main_container

    def toggleStyle(self, widget):
        self.main_progress.toggleStyle()

    def add(self, widget):
        self.main_progress.add(1)

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()