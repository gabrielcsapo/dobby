#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):

        main_container = dobby.Container()
        main_button = dobby.Button("Change Direction", on_click=self.changeDirection)
        main_container.add(main_button)
        main_container.constrain(main_button.TOP == main_container.TOP + 5)
        main_container.constrain(main_button.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(main_button.LEFT == main_container.LEFT + 5)

        left_container = dobby.Container()
        left_label = dobby.Label("I am the left label")
        left_container.add(left_label)
        left_container.constrain(left_label.TOP == left_container.TOP + 5)
        left_container.constrain(left_label.LEFT == left_container.LEFT + 5)

        right_container = dobby.Container()
        right_label = dobby.Label("I am the right label")
        right_container.add(right_label)
        right_container.constrain(right_label.TOP == right_container.TOP + 5)
        right_container.constrain(right_label.RIGHT == right_container.RIGHT - 5)

        self.split = dobby.SplitView()
        self.split.content = [left_container, right_container]

        main_container.add(self.split)
        main_container.constrain(self.split.TOP == main_button.BOTTOM + 15)
        main_container.constrain(self.split.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(self.split.LEFT == main_container.LEFT + 5)
        main_container.constrain(self.split.BOTTOM == main_container.BOTTOM)

        app.main_window.content = main_container

    def changeDirection(self, widget):
        self.split.changeDirection()

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()