import csv
from pathlib import Path


def cargar_ventas(path: Path):
    with path.open(encoding="utf-8-sig") as f:
        # Filtrar líneas vacías
        lineas = (line for line in f if line.strip())
        reader = csv.DictReader(lineas)
        return list(reader)
