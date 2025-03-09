print('Este programa te dice si un numero es par o impar. \n')
print('Primero ingresa el numero a comprobar. \n')

num = input('Numero > ')

def parOImpar(num):
    num = int(num)
    
    if ((num % 2) == 0):
        print('El numero ', num, ' ES par.')
    else:
        print('El numero ', num, ' NO es par.')
        
parOImpar(num)