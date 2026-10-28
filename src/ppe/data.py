"""Conversão de rótulos YOLO do SH17 para as classes do projeto."""
from pathlib import Path

CLASSES = ["person", "helmet", "glasses", "vest", "gloves", "boots"]
# índices do sh17.yaml oficial (não a ordem da tabela do README, que difere)
SH17_TO_PPE = {0: 0, 10: 1, 8: 2, 16: 3, 9: 4, 14: 5}


def remap_label(text: str) -> str:
    """Mantém só as classes do projeto e reindexa; linhas de outras classes são descartadas."""
    out = []
    for line in text.splitlines():
        parts = line.split()
        if parts and int(parts[0]) in SH17_TO_PPE:
            out.append(" ".join([str(SH17_TO_PPE[int(parts[0])])] + parts[1:]))
    return "\n".join(out) + ("\n" if out else "")


def convert_dir(src: Path, dst: Path) -> int:
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in src.glob("*.txt"):
        (dst / f.name).write_text(remap_label(f.read_text()))
        n += 1
    return n
