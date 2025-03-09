print('Este programa te dice el promedio de 3 numeros. \n')
print('Ingresa los numeros. \n')

num1 = input('Numero 1 > ')
num2 = input('Numero 2 > ')
num3 = input('Numero 3 > ')

def promedio(num1, num2, num3):
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    
    promedio = (num1 + num2 + num3) / 3
    
    print('El promedio de esos 3 numeros es ', promedio)
    
promedio(num1, num2, num3)