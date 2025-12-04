#Ejercicio de calculo de indice de masa corporal
print("Vamos a calcular tu indice de masa corporal IMC")

altura = float(input("Ingresa tu estatura en metros: "))
peso = float(input("Ingresa tu peso: "))

imc= peso / (altura ** 2)
print(f"Tu indice de masa corporal IMC es: {imc:0.2f}")