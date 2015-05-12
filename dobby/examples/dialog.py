import dobby

class Graze(dobby.App):

    def startup(self):
        
        self.dialog = dobby.Dialog()

        main_container = dobby.Container()
        info_button = dobby.Button("Info Dialog", on_click=self.showInfoDialog)
        main_container.add(info_button)
        main_container.constrain(info_button.TOP == main_container.TOP + 5)
        main_container.constrain(info_button.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(info_button.LEFT == main_container.LEFT + 5)

        confirm_button = dobby.Button("Confirm Dialog", on_click=self.showConfirmDialog)
        main_container.add(confirm_button)
        main_container.constrain(confirm_button.TOP == info_button.BOTTOM + 5)
        main_container.constrain(confirm_button.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(confirm_button.LEFT == main_container.LEFT + 5)

        error_button = dobby.Button("Error Dialog", on_click=self.showErrorDialog)
        main_container.add(error_button)
        main_container.constrain(error_button.TOP == confirm_button.BOTTOM + 5)
        main_container.constrain(error_button.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(error_button.LEFT == main_container.LEFT + 5)

        choice_button = dobby.Button("Choice Dialog", on_click=self.showChoiceDialog)
        main_container.add(choice_button)
        main_container.constrain(choice_button.TOP == error_button.BOTTOM + 5)
        main_container.constrain(choice_button.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(choice_button.LEFT == main_container.LEFT + 5)

        app.main_window.content = main_container

    def showInfoDialog(self, widget):
        self.dialog.info("Info", "This product is fully native")

    def showConfirmDialog(self, widget):
        result = self.dialog.confirm("Try it out?", "Would you like to try?")
        print(result)

    def showErrorDialog(self, widget):
        result = self.dialog.error("Button Error", "Error: You clicked this button...")
        print(result)

    def showChoiceDialog(self, widet):
        animals = ['Dog', 'Cat', 'Fish', 'Bee']
        result = self.dialog.choice("Favorite Animal", "What is your favorite animal?", animals)
        print(animals[result])

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()