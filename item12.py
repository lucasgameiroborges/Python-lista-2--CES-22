class Forma():
    def calc_area(self):
        pass

class Quadrado(Forma):
    def __init__(self,base):
        self.base = base

    def calc_area(self):
        print("area sem usar pi")
        return self.base * self.base

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calc_area(self):
        print("area usando pi")
        return self.raio * self.raio * 3.14


quad1 = Quadrado(1)
quad2 = Quadrado(1)
cir1 = Circulo(1)
cir2 = Circulo(1)

formas_geometricas = [quad1, quad2, cir1, cir2]

soma=0
# forma aqui é um objeto polimorfico, que pode assumir tanto a classe quadrado quanto a clase circulo
for forma in formas_geometricas:
    soma = soma + forma.calc_area()
    # independente do que a forma é (quadrado ou circulo) da pra usar o atributo calc_area (duck typing)

print("a area foi de {}".format(soma))
