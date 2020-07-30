import random
import PySimpleGUI


class DiceSimulator:
    # Values of the dice and message for users
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.message = 'Você gostaria de rolar o dado? (s / n)'

    # Receive response from users
    def start(self):
        response = input(self.message)
        try:
            if response == 's':
                self.dicevalue()
            elif response == 'n':
                print('Agradecemos sua particição!')
            else:
                print('Favor digitar "s" para sim e "n" para não!')
        except:
            print('Ocorreu um erro no programa.')

    # Show roll result
    def dicevalue(self):
        print(random.randint(self.min_value, self.max_value))


simulator = DiceSimulator()
simulator.start()
