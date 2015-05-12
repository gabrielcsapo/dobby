import dobby

class Graze(dobby.App):

    def startup(self):

        main_container = dobby.Container()
        main_password = dobby.PasswordInput(placeholder="Password")
        
        main_container.add(main_password)
        main_container.constrain(main_password.TOP == main_container.TOP + 5)
        main_container.constrain(main_password.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(main_password.LEFT == main_container.LEFT + 5)

        app.main_window.content = main_container

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()