#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):

        container = dobby.Container()
        self.tabContainer = dobby.TabContainer()
        container.add(self.tabContainer)
        container.constrain(self.tabContainer.LEFT == container.LEFT)
        container.constrain(self.tabContainer.RIGHT == container.RIGHT)
        container.constrain(self.tabContainer.TOP == container.TOP + 20)
        container.constrain(self.tabContainer.BOTTOM == container.BOTTOM)

        inputContainer = dobby.Container()
        inputContainer.add(dobby.Label("Currently in the input container"))
        graphContainer = dobby.Container()
        graphContainer.add(dobby.Label("Currently in the graph container"))
        self.tabContainer.add('Input', inputContainer)
        self.tabContainer.add('Graph', graphContainer)
        
        self.next = dobby.Button('Next', on_click=self.next)
        container.add(self.next)
        container.constrain(self.next.TOP == container.TOP + 5)
        container.constrain(self.next.RIGHT == container.RIGHT - 10)

        self.previous = dobby.Button('Previous', on_click=self.previous)
        container.add(self.previous)
        container.constrain(self.previous.TOP == container.TOP + 5)
        container.constrain(self.previous.LEFT == container.LEFT + 10)
        app.main_window.content = container

    def previous(self, widget):
        self.tabContainer.selectPreviousTabViewItem()

    def next(self, widget):
        self.tabContainer.selectNextTabViewItem()

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()