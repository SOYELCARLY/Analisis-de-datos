print("Vamos a hayar la media de 3 números")

tope = 0
datos = [{
    "numeros":[],
}]
while tope < 2:
    datos[tope] = int(input(f"Ingresa el numero{datos[tope]}: "))
    tope += 1

print(datos)