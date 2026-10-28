"""Associa EPIs detectados a pessoas e decide conformidade, incluindo ausência."""
from dataclasses import dataclass

# Zona vertical (fração da altura da pessoa, 0=topo) onde cada EPI deve estar.
ZONES = {
    "helmet": (0.0, 0.25),
    "glasses": (0.0, 0.25),
    "vest": (0.15, 0.65),
    "gloves": (0.25, 0.80),
    "boots": (0.80, 1.0),
}


@dataclass
class Person:
    track_id: int
    box: tuple  # x1, y1, x2, y2


@dataclass
class Item:
    cls: str
    box: tuple
    conf: float = 1.0


def _center(b):
    return (b[0] + b[2]) / 2, (b[1] + b[3]) / 2


def associate(person: Person, items: list, required: set) -> dict:
    """Retorna {classe: True/False} para cada EPI exigido.

    shortcut: ausência = "não detectado na zona"; não distingue oclusão de falta real,
    tratar com votação temporal por track_id (ver docs/plano) quando o pipeline existir.
    """
    x1, y1, x2, y2 = person.box
    h = y2 - y1
    found = {c: False for c in required}
    for it in items:
        if it.cls not in found or it.cls not in ZONES:
            continue
        cx, cy = _center(it.box)
        lo, hi = ZONES[it.cls]
        if x1 <= cx <= x2 and y1 + lo * h <= cy <= y1 + hi * h:
            found[it.cls] = True
    return found
