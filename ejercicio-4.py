print('Te pedire dos numeros y te dare el resultado de varias operaciones con ellos. \n')

num1 = input('Numero 1 > ')
num2 = input('Numero 2 > ')

def operar(num1, num2):
        resultadoSuma = int(num1) + int(num2)
        print('El resultado de esa suma es', resultadoSuma)
        
        resultadoResta = int(num1) - int(num2)
        print('El resultado de esa resta es', resultadoResta)
        
        resultadoMultiplicacion = int(num1) / int(num2)
        print('El resultado de esa division es', resultadoMultiplicacion)
        
        resultadoDivision = int(num1) * int(num2)
        print('El resultado de esa multiplicacion es', resultadoDivision)
        
operar(num1, num2)