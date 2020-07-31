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
                if int(self.given_value) > self.random_value:
                    print('Tente um valor menor!')
                    self.AskRandomValue()
                elif int(self.given_value) < self.random_value:
                    print('Tente um valor maior!')
                    self.AskRandomValue()
                if int(self.given_value) == self.random_value:
                    self.try_again = False
                    print('ACERTOU MIZERAVI !!')
        except:
            print('Apenas numero!')

    def AskRandomValue(self):
        self.given_value = input('Acerto o numero de 1 a 100: ')

    def GenRandomNumber(self):
        self.random_value = random.randint(self.min_value, self.max_value)


hit = HitTheNumber()
hit.start()
