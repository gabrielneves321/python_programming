COME_OF_AGE = 18

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if not self.age:
            return self.name
        return f'{self.name} ({self.age} yers old)'

    def is_adult(self):
        return (self.age or 0) > COME_OF_AGE

        