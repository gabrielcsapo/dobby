import dobby

class Graze(dobby.App):

    def startup(self):

        main_container = dobby.Container()
        main_button = dobby.Button("Change Direction", on_click=self.toggle_direction)
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

        self.splitView = dobby.SplitView()
        self.splitView.content = [left_container, right_container]

        main_container.add(self.splitView)
        main_container.constrain(self.splitView.TOP == main_button.BOTTOM + 15)
        main_container.constrain(self.splitView.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(self.splitView.LEFT == main_container.LEFT + 5)
        main_container.constrain(self.splitView.BOTTOM == main_container.BOTTOM)
        self.splitView.set_horizontal()

        app.main_window.content = main_container

    def toggle_direction(self, widget):
        self.splitView.toggle()

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()