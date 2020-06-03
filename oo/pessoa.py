class Pessoa:
    def __init__(self, nome=None, idade=49):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Ola!'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print (p.nome)
    p.nome = 'Paulo'
    print(p.nome)
    print(p.idade)





