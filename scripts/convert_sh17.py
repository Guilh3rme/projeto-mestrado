"""Uso: python scripts/convert_sh17.py <labels_sh17> <labels_saida>"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from ppe.data import convert_dir

print(convert_dir(Path(sys.argv[1]), Path(sys.argv[2])), "arquivos convertidos")
