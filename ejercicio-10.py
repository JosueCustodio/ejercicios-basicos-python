print("Crea un programa que pida al usuario una frase y cuente cuántas palabras contiene. (Pista: usa el método split()). \n")

frase = input('Escribe una frase > ')

numeroDePalabras = len(frase.split())

print(numeroDePalabras)