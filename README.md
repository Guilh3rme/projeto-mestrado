# Conformidade de EPI por pessoa, robusta a domínio e em borda

Mestrado — continuação do TCC (YOLOv8 + EPIs, Dom Bosco 2024). O TCC **detecta** EPIs; aqui o
sistema decide, **por trabalhador**, se cada EPI exigido está presente ou ausente.

## Pergunta de pesquisa
É possível verificar conformidade de EPI por pessoa de forma confiável em domínios adversos
(mineração, poeira, baixa luz) rodando em dispositivo de borda dentro de um orçamento de latência?

## Pipeline
`frame → detector (pessoa + EPIs) → associação EPI↔pessoa por zona corporal → conformidade/ausência por EPI exigido`
(tracker opcional, só no benchmark de borda; sem anotação própria não há avaliação temporal)

## Contribuições planejadas
1. **Associação com ausência**: lógica por zona do corpo, comparada a alternativas (containment/IoU, pose), com métrica por pessoa. Não é novidade absoluta; vale como comparação controlada.
2. **Robustez a domínio**: avaliação leave-one-domain-out e corrupções sintéticas (baixa luz, poeira/névoa, ruído, desfoque).
3. **Borda**: exportação ONNX/TensorRT (FP16/INT8), medindo latência p50/p95, FPS, memória e energia (Jetson).
4. **Dados**: apenas públicos (SH17, CHV, Construction-PPE, minersPPE se acessível); **sem coleta nem anotação própria**. Domínios = datasets distintos + corrupções sintéticas.

## Experimentos
| ID | O que | Métricas |
|----|-------|----------|
| E1 | Baseline do TCC re-treinado com split por cena | mAP50/50-95, P, R por classe |
| E2 | Detectores (YOLOv8/11 n,s,m) | mAP, latência |
| E3 | Associação por zona vs. alternativas | F1 de presença/ausência **por pessoa** (verdade derivada das caixas anotadas: EPI contido na caixa da pessoa) |
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
1. Classes definidas em `configs/ppe.yaml` (pessoa + 5 EPIs; ausência inferida pela associação).
2. Baixar SH17 (Kaggle) e usar `scripts/convert_sh17.py`; levantar datasets públicos extras e o do TCC.
3. Reproduzir E1 e fixar o baseline.
