def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(dobro, triplo)
    print(f'O triplo de 3 e {triplo(3)}')
    print(f'O dobro de 7 e {dobro(7)}')