class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')<strong>')
        return f'<span>{html}</spam>'

class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Animal:
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name + '(pet)' if self.pet else ''

class PeopleHtml(HtmlToStringMixin, People):
    pass

class AnimalHtml(HtmlToStringMixin, Animal):
    pass

if __name__ == '__main__':
    p1 = People('Tonny')
    print(p1)

    p2 = PeopleHtml('Michael')
    print(p2)

    rex = AnimalHtml('Rex')
    print(rex)
        