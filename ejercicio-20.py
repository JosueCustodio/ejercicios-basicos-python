# Ejercicio 20: Simulación de cajero automático
def cajero_automatico():
    monto = int(input("Ingrese el monto a retirar: "))
    if monto > 0 and monto % 10 == 0:
        billetes_50 = monto // 50
        resto = monto % 50
        billetes_20 = resto // 20
        resto %= 20
        billetes_10 = resto // 10
        print(f"Billetes de 50: {billetes_50}")
        print(f"Billetes de 20: {billetes_20}")
        print(f"Billetes de 10: {billetes_10}")
    else:
        print("Monto inválido. Debe ser positivo y múltiplo de 10.")

cajero_automatico()