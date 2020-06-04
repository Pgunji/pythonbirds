class Pessoa:
    def __init__(self, *filhos, nome='Paulo Jiro', idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Ola!'

if __name__ == '__main__':
    eduardo = Pessoa(nome='Eduardo')
    paulo = Pessoa(eduardo, nome='Paulo')

    print(Pessoa.cumprimentar(paulo))
    print(paulo.cumprimentar())
    print (paulo.nome)
    print(paulo.nome)
    print(paulo.idade)

    for filho in paulo.filhos:
        print(filho.nome)





