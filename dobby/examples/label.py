import dobby

class Graze(dobby.App):

    def startup(self):

        main_container = dobby.Container()
        main_label = dobby.Label(text="Testing", on_click=self.clickLabel, on_mouse_drag=self.dragLabel)
        
        main_container.add(main_label)
        main_container.constrain(main_label.TOP == main_container.TOP + 5)
        main_container.constrain(main_label.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(main_label.LEFT == main_container.LEFT + 5)

        app.main_window.content = main_container

    def clickLabel(self, widget):
        print('you are clicking label')

    def dragLabel(self, widget):
        print('you are dragging widget')

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()