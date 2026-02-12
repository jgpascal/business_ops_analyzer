from pathlib import Path
from ingestion import cargar_ventas


def calcular_importe(venta: dict) -> float:
    unidades = int(venta["unidades"])
    precio = float(venta["precio"])
    return unidades * precio


def total_por_tienda(ventas: list[dict]) -> dict:
    totales = {}

    for venta in ventas:
        tienda = venta["tienda"]
        totales.setdefault(tienda, 0)
        totales[tienda] += calcular_importe(venta)

    return totales


def main():
    print("Business Ops Analyzer iniciado")

    ventas = cargar_ventas(Path("data/ventas.csv"))
    print("Ventas cargadas:", ventas)

    importe_total = sum(calcular_importe(venta) for venta in ventas)
    print("Importe total de ventas:", importe_total)

    print("Ventas por tienda:", total_por_tienda(ventas))


if __name__ == "__main__":
    main()
