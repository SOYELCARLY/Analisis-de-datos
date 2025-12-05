print("Vamos a calcular tu calificación")
correctas = int(input("Numero de preguntas correctas: "))
incorrectas = int(input("Numero de preguntas incorrectas: "))
blanco = int(input("Numero de preguntas en blanco: "))

puntosCorrectas = 3
puntosIncorrectas = -1
puntosBlanco = 0

totalPuntos = ((puntosCorrectas*correctas) + (puntosIncorrectas*incorrectas))/ (correctas+incorrectas+blanco)
print(f"Tu puntaje final es {totalPuntos}")