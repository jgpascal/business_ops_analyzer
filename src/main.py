from pathlib import Path
from datetime import datetime
import csv

from ingestion import cargar_ventas
from processing import procesar_ventas

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

ventas_ok_path = REPORTS_DIR / f"ventas_ok_{timestamp}.csv"
errores_path = REPORTS_DIR / f"errores_{timestamp}.csv"


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

    data_path = BASE_DIR / "data" / "ventas.csv"

    print("BASE_DIR:", BASE_DIR)
    print("Data path:", data_path)
    print("Data path absolute:", data_path.resolve())
    print("Exists?", data_path.exists())


    print(f"Cargando ventas desde: {data_path}")
    ventas = cargar_ventas(data_path)

    print(f"Ventas crudas: {len(ventas)}")

    ventas_ok, errores = procesar_ventas(ventas)

    print(f"Ventas OK: {len(ventas_ok)}")
    print(f"Errores: {len(errores)}")

    campos_ok = ["fecha", "tienda", "producto", "unidades", "precio"]
    campos_error = ["index", "fecha", "tienda", "producto", "unidades", "precio", "error"]

    guardar_csv(ventas_ok_path, ventas_ok, campos_ok)
    guardar_csv(errores_path, errores, campos_error)

    print("Reportes generados:")
    print(ventas_ok_path)
    print(errores_path)



def guardar_csv(path, datos, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datos)
        





if __name__ == "__main__":
    main()
