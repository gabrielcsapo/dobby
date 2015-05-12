import dobby

class Graze(dobby.App):

    def startup(self):

        self.webview = dobby.WebView()

        self.url_input = dobby.TextInput('http://pybee.org/', on_keyUp=self.keyUp, on_endEditing=self.load_page)
        self.url_input.placeholder = 'http://...'

        self.webview.url = self.url_input.value
        self.go_button = dobby.Button('Go', on_click=self.load_page)
        left_image = dobby.Image('font-awesome/angle_left.png', width=20, height=15)
        self.go_back_button = dobby.Button('', image=left_image.get_image(), on_click=self.go_back)
        right_image = dobby.Image('font-awesome/angle_right.png', width=20, height=15)
        self.go_forward_button = dobby.Button('', image=right_image.get_image(), on_click=self.go_forward)

        container = dobby.Container()

        container.add(self.webview)
        container.add(self.url_input)
        container.add(self.go_button)
        container.add(self.go_back_button)
        container.add(self.go_forward_button)

        container.constrain(self.go_back_button.LEFT == container.LEFT + 5)
        container.constrain(self.go_back_button.TOP == container.TOP + 5)
        container.constrain(self.go_forward_button.LEFT == self.go_back_button.RIGHT)
        container.constrain(self.go_forward_button.TOP == container.TOP + 5)

        container.constrain(self.url_input.TOP == container.TOP + 5)
        container.constrain(self.url_input.LEFT == self.go_forward_button.RIGHT + 5)
        container.constrain(self.url_input.RIGHT + 5 == self.go_button.LEFT)

        container.constrain(self.go_button.TOP == container.TOP + 5)
        container.constrain(self.go_button.RIGHT + 5 == container.RIGHT)

        container.constrain(self.webview.TOP == self.url_input.BOTTOM + 20)
        container.constrain(self.webview.BOTTOM == container.BOTTOM)
        container.constrain(self.webview.RIGHT == container.RIGHT)
        container.constrain(self.webview.LEFT == container.LEFT)

        app.main_window.content = container

    def load_page(self, widget=None):
        self.webview.url = self.url_input.value

    def keyUp(self, key):
        if(key == 36):
            self.load_page()

    def go_back(self, widget):
        self.webview.go_back()

    def go_forward(self, widget):
        self.webview.go_forward()

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()