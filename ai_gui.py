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

            for x, row in enumerate(self.game.draw(bg='white', food='green', players='grey', head1='blue', head2='purple')):
                for y, cell in enumerate(row):
                    window[str(x * 100) + str(y)].update('█', text_color=cell)

            window.Refresh()
            time.sleep(0.1)

        window.close()
