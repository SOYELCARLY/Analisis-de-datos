print("Comprobamos si tu número es par o impar\n")

numero = int(input("Ingresa un número: "))

par = float(numero % 2)
#print(par)
if par == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El número {numero} es impar")