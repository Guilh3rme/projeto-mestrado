# Conformidade de EPI por pessoa, robusta a domínio e em borda

Mestrado — continuação do TCC (YOLOv8 + EPIs, Dom Bosco 2024). O TCC **detecta** EPIs; aqui o
sistema decide, **por trabalhador**, se cada EPI exigido está presente ou ausente.

## Pergunta de pesquisa
É possível verificar conformidade de EPI por pessoa de forma confiável em domínios adversos
(mineração, poeira, baixa luz) rodando em dispositivo de borda dentro de um orçamento de latência?

## Pipeline
`vídeo → detector (pessoa + EPIs) → tracker (ByteTrack) → associação EPI↔pessoa por zona corporal
→ votação temporal por track_id → conformidade/ausência por EPI exigido`

## Contribuições planejadas
1. **Associação com ausência**: lógica por zona do corpo + suavização temporal (separa oclusão de falta real).
2. **Robustez a domínio**: avaliação leave-one-domain-out e corrupções sintéticas (baixa luz, poeira/névoa, ruído, desfoque).
3. **Borda**: exportação ONNX/TensorRT (FP16/INT8), medindo latência p50/p95, FPS, memória e energia (Jetson).
4. **Dataset**: divisão por vídeo/cena (sem vazamento), documentado e, se possível, aberto.

## Experimentos
| ID | O que | Métricas |
|----|-------|----------|
| E1 | Baseline do TCC re-treinado com split por cena | mAP50/50-95, P, R por classe |
| E2 | Detectores (YOLOv8/11 n,s,m) | mAP, latência |
| E3 | Associação + temporal vs. sem temporal | F1 de presença/ausência **por pessoa** |
| E4 | Shift de domínio (LODO + corrupções) | queda de mAP/F1 vs. in-domain |
| E5 | Mitigação (augmentation de domínio, fine-tune, realce) | recuperação do F1 |
| E6 | Borda: PyTorch→ONNX→TensorRT FP16/INT8 | latência p50/p95, FPS, ΔmAP |

## Ambiente
**Execução pesada (treino, benchmark) no Google Colab**: use `notebooks/colab_setup.ipynb`. O PC local é só para editar código e rodar testes leves.

- Treino: RTX 4060 Ti 8 GB. Borda alvo: Jetson (a definir o modelo).
- Python 3.12 (3.14 ainda sem wheels do PyTorch).

```bash
uv venv --python 3.12 && source .venv/bin/activate   # ou python3.12 -m venv .venv
pip install -e ".[dev]" && pytest
```

## Estrutura
`src/ppe/` código · `tests/` · `configs/` YAMLs de dados/treino · `scripts/` treino, avaliação, benchmark · `docs/` notas · `data/` (ignorado pelo git)

## Plano
Ver [`docs/plano-macro.md`](docs/plano-macro.md) (fases 0–7).

## Próximos passos
1. Definir classes e esquema de anotação (pessoa + 5 EPIs; avaliar classes "sem capacete" etc.).
2. Levantar datasets públicos (ex.: SH17, CHV, SHWD) e reaproveitar o dataset do TCC.
3. Reproduzir E1 e fixar o baseline.
