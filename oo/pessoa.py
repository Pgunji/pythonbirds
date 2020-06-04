class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome='Paulo Jiro', idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Ola!'

    @staticmethod
    def metodo_estatico():
        return 1000

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos ={cls.olhos} '

if __name__ == '__main__':
    eduardo = Pessoa(nome='Eduardo')
    paulo = Pessoa(eduardo, nome='Paulo')

    print(Pessoa.cumprimentar(paulo))
    print(paulo.cumprimentar())
    print (paulo.nome)
    print(paulo.idade)

    for filho in paulo.filhos:
        print(filho.nome)

    paulo.sobrenome = 'Gunji'
    del paulo.idade
    print (paulo.__dict__)
    print(eduardo.__dict__)
    paulo.olhos =1

    print(Pessoa.olhos)
    print(paulo.olhos)
    print(eduardo.olhos)

    print(Pessoa.nome_e_atributos_de_classe(), paulo.nome_e_atributos_de_classe())







