import dobby

class Graze(dobby.App):

    def startup(self):

        container = dobby.Container()
        self.textview = dobby.TextView()
        self.textview.setRichText(True)
        self.textview.setImportsGraphics(True)
        print(self.textview.importsGraphics())
        container.add(self.textview)
        container.constrain(self.textview.LEFT == container.LEFT)
        container.constrain(self.textview.RIGHT == container.RIGHT)
        container.constrain(self.textview.TOP == container.TOP + 20)
        container.constrain(self.textview.BOTTOM == container.BOTTOM)
        print(self.textview.backgroundColor())
        app.main_window.content = container

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()