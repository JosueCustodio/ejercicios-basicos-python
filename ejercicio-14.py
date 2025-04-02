# Ejercicio 14: Determinar si es vocal o consonante
def tipo_letra():
    letra = input("Ingrese una letra: ").lower()
    if letra in "aeiou":
        print("Es una vocal.")
    elif letra.isalpha():
        print("Es una consonante.")
    else:
        print("No es una letra válida.")

tipo_letra()