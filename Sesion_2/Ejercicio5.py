print("Multiplicaciones acumuladas")
lista = []
numero = 0
while numero < 10:
    numero = int(input("Ingresa un numero entero entre 1 y 10 "))
    if numero < 10:
        lista.append(numero)
    else:
        total = 1
        for valor in lista:
            total = total * valor
print(total)


