class Humano:

    especie = 'homo sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'homo neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'José.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')