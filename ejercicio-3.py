import math

print('Este programa te dice el area de un circulo usando su radio. \n')
print('Para empezar, prporcioname el radio. \n')

radio = input('Intoduce el radio del circulo > ')

def areaCirculo(radio):
    radio = int(radio)
    pi = math.pi
    area = pi * radio ** 2
    print('El area del circulo es de ', area)

areaCirculo(radio)