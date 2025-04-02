# Ejercicio 17: Sumar números pares del 1 al 100 con while
def suma_pares():
    suma = 0
    num = 2
    while num <= 100:
        suma += num
        num += 2
    print(f"La suma de los números pares del 1 al 100 es {suma}.")

suma_pares()