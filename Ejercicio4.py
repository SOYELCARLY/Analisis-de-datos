print("Vamos a determinar la dimension del tornillo")
medida = float(input("Ingresa la medida del tornillo: "))

#valor_float = float(valor.replace(",", "."))

if medida > 0:
    if medida >= 1 and medida < 3:
        print("es pequeño")
    elif medida >= 3 and medida < 5:
        print("es mediano")
    elif medida >=5 and medida < 6.5:
        print("es grande")
    elif medida >= 6.5 and medida < 8.5:
        print("es muy grande")
    elif medida >= 8.5:
        print("es gigante")
    else:
        print("medida inexistente")