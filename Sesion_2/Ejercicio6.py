print("Vamos a visualizar la serie fibonacci")

def fibonacci(numero):
    serie = []
    
    for num in range(numero):
        if num == 0:
            serie.append(0)
        elif num == 1:
            serie.append(1)
        else:
            serie.append(serie[num-1] + serie[num-2])
    return serie

rango = int(input("Ingrese cuantos numeros de la serie desea imprimir: "))
print(f"Los primeros {rango}  elementos de la serie Fibonacci son:", fibonacci(rango))
