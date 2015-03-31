#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):

        container = dobby.Container()

        self.table = dobby.TableView(['First Name', 'Last Name'], on_selection_change=self.onChange)
        self.table.insert(None, 'John', 'Doe')
        self.table.insert(None, 'Jane', 'Doe')
        self.table.insert(None, 'Py', 'Bee')
        container.add(self.table)
        container.constrain(self.table.LEFT == container.LEFT)
        container.constrain(self.table.RIGHT == container.RIGHT)
        container.constrain(self.table.TOP == container.TOP + 40)
        container.constrain(self.table.BOTTOM == container.BOTTOM)

        self.saveData = dobby.Button("Save Data", on_click=self.getValues)
        container.add(self.saveData)
        container.constrain(self.saveData.TOP == container.TOP + 10)
        container.constrain(self.saveData.LEFT == container.LEFT + 10)

        app.main_window.content = container

    def onChange(self, notification):
        print('selection changed')

    def getValues(self, widget):
        print(self.table.getData())

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()