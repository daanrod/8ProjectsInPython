import random
import PySimpleGUI as sg


class DiceSimulator:
    # Values of the dice and message for users
    def __init__(self):
        self.min_value = 1
        self.max_value = 6

        # Layout
        self.layout = [
            [sg.Text('Rolar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        # Create a window
        self.window = sg.Window('Simulador de dado', self.layout)

        # Read values
        self.events, self.values = self.window.Read()

    # Receive response from users
    def start(self):
        # Do something with this values
        if self.events == 'Sim':
            self.dicevalue()
        elif self.events == 'Não':
            print('Agradecemos sua particição!')

    # Show roll result
    def dicevalue(self):
        print(random.randint(self.min_value, self.max_value))


simulator = DiceSimulator()
simulator.start()
