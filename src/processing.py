from datetime import datetime

def validar_y_normalizar_venta(venta):
    
    campos_obligatorios = ["fecha", "tienda", "producto", "unidades", "precio"]
    for campo in campos_obligatorios:
       if campo not in venta or not venta[campo]:
            raise ValueError(f"El campo '{campo}' es obligatorio y no puede estar vacío.")
    tienda = venta["tienda"].strip()
    producto = venta["producto"].strip()
    fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d").date()
    unidades = int(venta["unidades"])
    if unidades <= 0:
        raise ValueError(f"La cantidad {unidades} debe ser mayor que cero")
    precio = float(venta["precio"])
    if precio <= 0:
        raise ValueError(f"El precio {precio} no puede ser cero o negativo")
    
    return {
        "tienda" : tienda,
        "producto" : producto,
        "fecha" : fecha,
        "unidades" : unidades,
        "precio" : precio
    }


def procesar_ventas(ventas_crudas):
        ventas_ok = []
        errores = []
        for i, venta in enumerate(ventas_crudas):
            try:
                venta_normalizada = validar_y_normalizar_venta(venta)
                ventas_ok.append(venta_normalizada)
            
            except Exception as e:
                errores.append({
                     "index": i,
                     "venta": venta,
                     "error": str(e),
                    })
                
        return ventas_ok, errores