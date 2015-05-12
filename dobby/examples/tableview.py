import dobby

class Graze(dobby.App):

    def startup(self):

        container = dobby.Container()

        self.table = dobby.TableView(['First Name', 'Last Name'], on_selection_change=self.on_change)
        self.table.insert(None, 'John', 'Doe')
        self.table.insert(None, 'Jane', 'Doe')
        self.table.insert(None, 'Py', 'Bee')
        container.add(self.table)
        container.constrain(self.table.LEFT == container.LEFT)
        container.constrain(self.table.RIGHT == container.RIGHT)
        container.constrain(self.table.TOP == container.TOP + 40)
        container.constrain(self.table.BOTTOM == container.BOTTOM)

        self.btnSaveData = dobby.Button("Save Data", on_click=self.get_values)
        container.add(self.btnSaveData)
        container.constrain(self.btnSaveData.TOP == container.TOP + 10)
        container.constrain(self.btnSaveData.LEFT == container.LEFT + 10)

        app.main_window.content = container

    def on_change(self, notification):
        print('selection changed')

    def get_values(self, widget):
        print(self.table.get_data())

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()