from .people import People

class Seller(People):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.wage = wage