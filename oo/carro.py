class Motor:
    tipo = 'Etanol'
    potencia = 1.5


class Carro(Motor):

    def __init__(self,v,c,l):
        self.cor = c
        self.ligado=l
        self.vel = v
    def info(self):
        print('Velocidade = ' + str(self.vel))
        print('Cor = ' + self.cor)
        print('Ligado =' + str(self.ligado))
        print('Tipo = ' + self.tipo)
        print('---------------------------------')


        
c1= Carro(100,"Azul",True)
c2= Carro(200,"Preto", False)
c3= Carro(80,"Laranja", True)
c1.tipo = 'Gasolina'

c1.info()
c2.info()













