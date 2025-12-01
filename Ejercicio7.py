print("Piezas aptas de un lote")

tope = int(input("Cuantas piezas vas a registrar? "))
aptas = 0

for i in range(tope):
    pieza = float(input(f"Ingrese la dimension de la pieza {i+1}: "))
    comprueba = pieza
    if comprueba >= 1.20 and comprueba <= 1.30:
        print("Hola ",comprueba)
        aptas = aptas + 1
        print("aptas ",aptas)
        comprueba = 0
    i =+ 1

print(f"La cantidad de piezas aptas es: {aptas}")