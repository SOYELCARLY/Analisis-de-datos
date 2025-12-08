import pandas as pd
nombres = []
valores = []
print("Impresion de tu factura\n")


sale = ""
while sale != "fin":
    articulo = str(input("Ingresa el nombre del articulo: "))
    nombres.append(articulo)
    sale = articulo.lower()
    if sale == "fin":
        nombres.pop()
        bill = {
            "nombre" : nombres,
            "valor" : valores, 
        }
        resultados = []
        resultados.append("TOTAL")
        df = pd.DataFrame(bill)
        precioTotal = float(df["valor"].sum())
        resultados.append(precioTotal)  
        print(df,resultados)
    else:
        valores.append(float(input("Ingresa el valor del articulo: ")))
    


        
