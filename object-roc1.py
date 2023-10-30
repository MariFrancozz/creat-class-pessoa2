# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
#Criando instancia da classe Rocket
roc1 =Rocket(10, 20)

#Chamando os atributos
roc1.x
roc1.y

#chamando os métodos
roc1.move_rocket(11, 32)

roc1.print_rocket()