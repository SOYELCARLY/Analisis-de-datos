import pandas as pd
print("Vamos a hayar la media de 3 números")

tope = 0
numeros = []

numeros.append(int(input("Ingresa el número 1: ")))
numeros.append(int(input("Ingresa el número 2: ")))
numeros.append(int(input("Ingresa el número 3: ")))

df = pd.DataFrame(numeros)
print(df.median())
