celsius = input('Escribe los grados Celsius > ')

def conventir (grados = celsius):
    grados = float(grados)
    fahrenheit = (grados * (9 / 5) + 32)
    print(celsius + ' grados Celsius son ' + str(fahrenheit) + ' grados Fahrenheit')
    
conventir(celsius)