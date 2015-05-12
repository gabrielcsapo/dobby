#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

import dobby

class Graze(dobby.App):

    def startup(self):

        self.dialog = dobby.Dialog()

        left_container = dobby.Container()
        self.basic_button = dobby.Button("Basic Button", on_click=self.buttonChange)
        left_container.add(self.basic_button)
        left_container.constrain(self.basic_button.TOP == left_container.TOP + 5)
        left_container.constrain(self.basic_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.basic_button.LEFT == left_container.LEFT + 5)

        self.momentary_button = dobby.Button("Momentary Button", on_click=self.buttonChange)
        self.momentary_button.set_style('NSMomentaryLightButton')
        left_container.add(self.momentary_button)
        left_container.constrain(self.momentary_button.TOP == self.basic_button.BOTTOM + 5)
        left_container.constrain(self.momentary_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.momentary_button.LEFT == left_container.LEFT + 5)

        self.toggle_button = dobby.Button("Toggle Button", on_click=self.buttonChange)
        self.toggle_button.set_style('NSToggleButton')
        left_container.add(self.toggle_button)
        left_container.constrain(self.toggle_button.TOP == self.momentary_button.BOTTOM + 5)
        left_container.constrain(self.toggle_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.toggle_button.LEFT == left_container.LEFT + 5)

        self.switch_button = dobby.Button("Switch Button", on_click=self.buttonChange)
        self.switch_button.set_style('NSPushOnPushOffButton')
        left_container.add(self.switch_button)
        left_container.constrain(self.switch_button.TOP == self.toggle_button.BOTTOM + 5)
        left_container.constrain(self.switch_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.switch_button.LEFT == left_container.LEFT + 5)

        self.radio_button = dobby.Button("Radio Button", on_click=self.buttonChange)
        self.radio_button.set_style('NSRadioButton')
        left_container.add(self.radio_button)
        left_container.constrain(self.radio_button.TOP == self.switch_button.BOTTOM + 5)
        left_container.constrain(self.radio_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.radio_button.LEFT == left_container.LEFT + 5)

        self.radio_button_2 = dobby.Button("Radio Button", on_click=self.buttonChange)
        self.radio_button_2.set_style('NSRadioButton')
        left_container.add(self.radio_button_2)
        left_container.constrain(self.radio_button_2.TOP == self.switch_button.BOTTOM + 5)
        left_container.constrain(self.radio_button_2.LEFT == self.radio_button.LEFT + 100)

        self.momentary_change_button = dobby.Button("Momentary Change Button", on_click=self.buttonChange)
        self.momentary_change_button.set_style('NSMomentaryChangeButton')
        left_container.add(self.momentary_change_button)
        left_container.constrain(self.momentary_change_button.TOP == self.radio_button.BOTTOM + 5)
        left_container.constrain(self.momentary_change_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.momentary_change_button.LEFT == left_container.LEFT + 5)

        self.on_off_button = dobby.Button("On Off Button", on_click=self.buttonChange)
        self.on_off_button.set_style('NSOnOffButton')
        left_container.add(self.on_off_button)
        left_container.constrain(self.on_off_button.TOP == self.momentary_change_button.BOTTOM + 5)
        left_container.constrain(self.on_off_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.on_off_button.LEFT == left_container.LEFT + 5)

        self.momentary_pushin_button = dobby.Button("Momentary Push in Button", on_click=self.buttonChange)
        self.momentary_pushin_button.set_style('NSMomentaryPushInButton')
        left_container.add(self.momentary_pushin_button)
        left_container.constrain(self.momentary_pushin_button.TOP == self.on_off_button.BOTTOM + 5)
        left_container.constrain(self.momentary_pushin_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.momentary_pushin_button.LEFT == left_container.LEFT + 5)

        right_image = dobby.Image('font-awesome/apple22.png', width=20, height=15)
        self.image_button = dobby.Button('', image=right_image.get_inst(), on_click=self.buttonChange)
        left_container.add(self.image_button)
        left_container.constrain(self.image_button.TOP == self.momentary_pushin_button.BOTTOM + 5)
        left_container.constrain(self.image_button.RIGHT == left_container.RIGHT - 5)
        left_container.constrain(self.image_button.LEFT == left_container.LEFT + 5)

        right_container = dobby.Container()
        self.table = dobby.TableView(['Button Name', 'State'])
        right_container.add(self.table)
        right_container.constrain(self.table.TOP == right_container.TOP + 5)
        right_container.constrain(self.table.RIGHT == right_container.RIGHT - 5)
        right_container.constrain(self.table.LEFT == right_container.LEFT + 5)
        right_container.constrain(self.table.BOTTOM == right_container.BOTTOM + 5)

        self.split = dobby.SplitView()
        self.split.content = [left_container, right_container]
        self.split.set_vertical()

        app.main_window.content = self.split

    def buttonChange(self, widget):
        data = []
        data.append(['basic_button', str(self.basic_button.state())])
        data.append(['momentary_button', str(self.momentary_button.state())])
        data.append(['toggle_button', str(self.toggle_button.state())])
        data.append(['switch_button', str(self.switch_button.state())])
        data.append(['radio_button', str(self.radio_button.state())])
        data.append(['radio_button_2', str(self.radio_button_2.state())])
        data.append(['momentary_change_button', str(self.momentary_change_button.state())])
        data.append(['on_off_button', str(self.on_off_button.state())])
        data.append(['momentary_pushin_button', str(self.momentary_pushin_button.state())])
        data.append(['image_button', str(self.image_button.state())])
        self.table.setData(data)

if __name__ == '__main__':
    app = Graze('Graze', 'org.pybee.graze')
    app.main_loop()