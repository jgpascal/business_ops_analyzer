def main():
    print("Business Ops Analyzer iniciado")


if __name__ == "__main__":
    main()



print ("Ingrese datos de venta")
tienda = input ("Tienda ? ")
producto = input ("Producto ? ")
unidades = int (input ("Cantidad ? "))
precio = int (input ("Precio unitario ? "))
venta = {"tienda":tienda, "producto":producto, "unidades":unidades, "precio":precio}

# print (venta)

def calcular_importe(venta):
    
    return venta["unidades"] * venta["precio"]

print ("Importe de la venta: ", calcular_importe(venta))



def total_por_tienda(ventas):
    totales = {}

    for venta in ventas:
        tienda = venta["tienda"]
        totales.setdefault(tienda, 0)
        totales[tienda] += calcular_importe(venta)

    return totales

print ("Ventas por tienda:", total_por_tienda([venta]))