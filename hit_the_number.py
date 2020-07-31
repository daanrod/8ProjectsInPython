import random


class HitTheNumber:
    def __init__(self):
        self.random_value = 0
        self.min_value = 1
        self.max_value = 100
        self.try_again = True

    def start(self):
        self.GenRandomNumber()
        self.AskRandomValue()
        try:
            while self.try_again:
                # Informs if the given value is higher than correct value
                if int(self.given_value) > self.random_value:
                    print('Tente um valor menor!')
                    self.AskRandomValue()
                # Informs if the given value is lower than the correct value
                elif int(self.given_value) < self.random_value:
                    print('Tente um valor maior!')
                    self.AskRandomValue()
                # Informs thats the correctly value
                if int(self.given_value) == self.random_value:
                    self.try_again = False
                    print('ACERTOU MIZERAVI !!')
        except:
            print('Apenas numero!')

    # Ask a value
    def AskRandomValue(self):
        self.given_value = input('Acerto o numero de 1 a 100: ')

    # Generates a random value
    def GenRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)


hit = HitTheNumber()
hit.start()
