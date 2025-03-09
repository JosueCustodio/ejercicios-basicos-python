print('Escribe un programa que determine si un número ingresado por el usuario es positivo, negativo o cero. \n')

numero = int(input('Escribe el numero > '))


if (numero > 0):
    print(numero, ' es POSITIVO')
elif (numero < 0):
    print(numero, ' es NEGATIVO')
elif (numero == 0):
    print(numero, ' es CERO')