print("Informe de pagos emrpesarial")
print("\nNOTA: Los saldos son entre 100 y 500\n")

sueldos = []
rangoSueldo1 = 0
rangoSueldo2 = 0
totalSueldos = 0
gastoEmpresa = 0

tope = int(input("Cuantos sueldos vas a ingresar? "))

for i in range(tope):
    valor = float(input(f"Ingresa el sueldo {i+1} "))
    if valor > 100 and valor <=300:
        rangoSueldo1 =+1
    elif valor > 300:
        rangoSueldo2 =+ 1
    sueldos.append(valor)
    i =+ 1
    

totalSueldos = sum(sueldos)

print(f"Esta es la cantidad que cobran entre 100 y 300: {rangoSueldo1}")
print(f"Esta es la cantidad que cobran mas de 300: {rangoSueldo2}")
print(f"Estos son los sueldos que ingresaste: \n{sueldos}")
print(f"Este es la suma total de sueldos: \n{totalSueldos}")