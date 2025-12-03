print("Quieres saber que tipo de triangulo tienes? Ingresa los lados y te indico cual es\n")

lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))

if lado1 == lado2 and lado1 == lado3 :
    print("Es un tringulo equilatero")
elif lado1 == lado2 and lado1 != lado3:
    print("Es un triangulo isoseles")
elif lado1 == lado3 and lado1 != lado2:
    print("Es un triangulo isoseles")
elif lado2 == lado3 and lado2 != lado1:
    print("Es un triangulo isoseles")
else:
    print("Es un triangulo escaleno")

