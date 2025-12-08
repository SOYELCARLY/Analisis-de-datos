import pandas as pd
print("\nAsociación de notas a las asignaciones")
print("Vas a ir ingresando los nombres de las materias, uno a uno:")
print("Para salir escribe 'OK' en cualquiera de las dos secciones\n")

materias = []
notas = []
sale = "no"
count = 0
while sale != "ok":
    valor = str(input(f"Ingresa el nombre de la materia {count+1}: "))
    valor = valor.lower()
    if valor == "ok":
      sale = "ok"
    else:
        materias.append(valor)
    count += 1

#print(f"materias: {materias}")
print("\nAhora ingresa las notas")
print(f"Recuerda que debes ingresar {len(materias)} notas\n")
sale = len(materias)
count2 = 0

while count2 < sale:
    valor = float(input(f"Ingresa la nota No. {count2+1}: "))
    notas.append(valor)
    count2 += 1

asignaciones = {
    "materias" : materias,
    "notas" : notas,
}

df = pd.DataFrame(asignaciones)
for i in range(sale):
    print(f"En {df["materias"][i]} has sacado {df["notas"][i]}")
#print(asignaciones)