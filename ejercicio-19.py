# Ejercicio 19: Calcular el factorial de un número
def calcular_factorial():
    num = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")

calcular_factorial()