import PySimpleGUI as SimpleGui
import time


class GameRenderer:
    def __init__(self, game, window_color='Dark Blue 3'):
        SimpleGui.change_look_and_feel(window_color)

        self.game = game

        # All the stuff inside your window.
        self.layout = []

        for x, row in enumerate(self.game.draw()):
            curr_row = []
            for y, cell in enumerate(row):
                curr_row.append(SimpleGui.Text(cell, key=str(x*100) + str(y)))
            self.layout.append(curr_row)

        self.layout.append([SimpleGui.Button('Start')])

    def render(self, max_length):
        # Create the Window
        window = SimpleGui.Window('Snake Battle', self.layout)
        # Event Loop to process "events" and get the "values" of the inputs
        window.Read()

        for i in range(max_length):
            self.game.update()

            if self.game.done:
                window.close()
                return False

            for x, row in enumerate(self.game.draw()):
                for y, cell in enumerate(row):
                    curr_color = 'white'

                    # bg='# ', food='@ ', players='O ', head1='A ', head2='B '
                    if '@' in cell:
                        curr_color = 'green'

                    if 'O' in cell:
                        curr_color = 'grey'

                    if 'A' in cell:
                        curr_color = 'blue'

                    if 'B' in cell:
                        curr_color = 'purple'

                    window[str(x * 100) + str(y)].update(cell, text_color=curr_color)

            window.Refresh()
            # time.sleep(sleep_value)

        window.close()
