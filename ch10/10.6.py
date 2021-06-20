
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('(', self.name, ",", self.symbol, ",", self.number, ")")

dl_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**dl_dict)
hydrogen.dump()
