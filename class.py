

class Flower:
    #constructor, init=initial
    def __init__(self, name):
        self.name = name
        self.pet = int(input(f'How many petals it has?'))
        self.price = self.pet*5000


    def data(self):
        print(f'The name is {self.name} and the price: {self.price}')

rose = Flower('Rose')
rose.data()