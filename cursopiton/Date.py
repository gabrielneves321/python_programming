class Date:
    def __str__(self):
        return f'{self.day}/{self.mounth}/{self.year}'


d1 = Date()
d1.day = 14
d1.mounth = 11
d1.year = 2003
print(d1)

d2 = Date()
d2.day = 21
d2.mounth = 12
d2.year = 1980
print(d2)
    
