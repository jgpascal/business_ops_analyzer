import csv
from pathlib import Path


def cargar_ventas(path: Path):
    with path.open() as f:
        reader = csv.DictReader(f)
        return list(reader)
