print("Calculamos tu inversion")

monto = float(input("Ingrese la cantidad a invertir: "))
time = int(input("Ingrese el número de años: "))
interes = float(input("Ingrese el interés anual (%): "))


for num in range(time):
    gana = monto * (interes/100)
    monto = round((gana + monto),2)
    print(f"Año {num+1}: Capital acumulado = {monto}")

print(f"El monto total a recibir es de: ${monto:0.2f}")