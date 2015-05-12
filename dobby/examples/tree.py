import dobby

class Graze(dobby.App):

    def startup(self):

    	main_container = dobby.Container()

    	left_container = dobby.Container()

    	label = dobby.Label("Tree View")
    	left_container.add(label)
    	left_container.constrain(label.TOP == left_container.TOP + 5)
        left_container.constrain(label.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(label.LEFT == left_container.LEFT + 5)

        self.tree = dobby.Tree(['Test'])
        left_container.add(self.tree)
        root1 = self.tree.insert(None, None, 'root1')
        root2 = self.tree.insert(None, None, 'root2')
        root2_1 = self.tree.insert(root2, None, 'root2.1')
        root2_2 = self.tree.insert(root2, None, 'root2.2')
        root2_2_1 = self.tree.insert(root2_2, None, 'root2.2.1')
        root2_2_2 = self.tree.insert(root2_2, None, 'root2.2.2')
        root2_2_3 = self.tree.insert(root2_2, None, 'root2.2.3')
        root2_3 = self.tree.insert(root2, None, 'root2.3')
        root3 = self.tree.insert(None, None, 'root3')
        root2_4 = self.tree.insert(root2, 1, 'root2.4')

        left_container.constrain(self.tree.TOP == label.BOTTOM + 5)
        left_container.constrain(self.tree.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.tree.LEFT == left_container.LEFT + 5)
        left_container.constrain(self.tree.BOTTOM == left_container.BOTTOM - 10)

        right_container = dobby.Container()

        self.split = dobby.SplitView()
        self.split.set_vertical()
        self.split.content = [left_container, right_container]

        main_container.add(self.split)
        main_container.constrain(self.split.TOP == main_container.TOP)
        main_container.constrain(self.split.RIGHT == main_container.RIGHT - 5)
        main_container.constrain(self.split.LEFT == main_container.LEFT + 5)
        main_container.constrain(self.split.BOTTOM == main_container.BOTTOM)
        app.main_window.content = main_container

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()