# Projeto de mestrado: conformidade de EPI por pessoa (detecção, rastreamento, associação, borda)

Contexto: `README.md` (pergunta de pesquisa, pipeline, experimentos) e `docs/plano-macro.md` (fases 0–7).
Os planos detalhados ficam em `docs/fase-N-<nome>.md`. Leia a fase corrente antes de agir.

## Comandos
- Treino/avaliação pesados rodam no **Colab** (`notebooks/colab_setup.ipynb`), não no PC local; dados e `runs/` ficam no Drive.
- Ambiente: Python 3.12 (`python3 -m venv .venv` só com 3.12; o 3.14 do sistema não serve para PyTorch).
- Instalar: `pip install -e ".[dev]"`
- Testes: `pytest` · Lint/format: `ruff check . && ruff format .`

## Regras do projeto
- Pesquisa reproduzível: seeds fixas, configs em `configs/`, resultados em `runs/` (ignorado pelo git). Nunca reportar métrica sem comando/config que a gere.
- O conjunto de teste fica intocado até a Fase 6. Divisão sempre por vídeo/cena, nunca por frame; augmentation só depois do split.
- Não versionar dados, pesos (`.pt`, `.onnx`, `.engine`) nem segredos. Respeitar licenças e LGPD dos dados.
- Código pequeno e testado; atalhos conhecidos marcados com `# shortcut: <limite>, <quando melhorar>`.
- Afirmações de literatura precisam de fonte verificada. Não citar de memória.

## Skills e plugins: quando usar
Use só o que a tarefa pede; não rode todos os workflows em toda tarefa.

| Situação | Use |
|---|---|
| Revisão de literatura, datasets públicos, comparação de trabalhos | `anthropic-skills:deep-research` |
| Docs oficiais do Ultralytics/PyTorch/TensorRT antes de implementar | `agent-skills:source-driven-development` |
| Especificar uma fase ou módulo antes de codar | `agent-skills:spec` / `spec-driven-development` |
| Quebrar uma fase em tarefas | `agent-skills:plan` |
| Implementar em fatias pequenas com teste | `agent-skills:build`, `incremental-implementation` |
| Lógica nova (associação, tracking, métricas) | `agent-skills:test-driven-development` |
| Treino/inferência quebrando, métricas estranhas | `agent-skills:debugging-and-error-recovery` |
| Decisões de arquitetura/metodologia (registrar o porquê) | `agent-skills:documentation-and-adrs` → `docs/adr/` |
| Revisar mudanças antes de consolidar | `agent-skills:review` ou `code-review` |
| Gargalo de latência na borda | `agent-skills:performance-optimization` |
| Dados de trabalhadores, privacidade, dependências | `agent-skills:security-and-hardening` |
| Limites de qualidade (cobertura, lint, latência máxima) | `agent-skills:constraints` → `CONSTRAINTS.md` |
| Commits e branches | `agent-skills:git-workflow-and-versioning` |
| Gráficos de resultados (PR, degradação por severidade, Pareto) | `dataviz` |
| Entender dependências entre módulos quando o código crescer | `graphify` (só sobre `src/`, nunca `data/`, `runs/` ou `.venv/`) |
| Lido/gerado: artigos e relatórios em PDF/Word, tabelas em Excel | `anthropic-skills:pdf`, `docx`, `xlsx` |
| Simplicidade, evitar over-engineering | `ponytail:ponytail` (modo ativo) |

Observações:
- Playwright e skills de animação/UI não se aplicam a este projeto, a menos que surja um dashboard ou demo web.
- Sub-agentes (`agent-skills:code-reviewer`, `test-engineer`, `security-auditor`) só quando eu pedir revisão explícita.

## Skills por fase (atalho)
- **0 Fundação:** `deep-research`, `spec`, `documentation-and-adrs`, `constraints`
- **1 Dados:** `deep-research`, `security-and-hardening` (LGPD/licenças), `test-driven-development` (split sem vazamento)
- **2 Baseline:** `source-driven-development`, `build`, `dataviz`
- **3 Associação:** `spec`, `test-driven-development`, `debugging-and-error-recovery`
- **4 Robustez:** `build`, `dataviz`, `deep-research`
- **5 Borda:** `source-driven-development`, `performance-optimization`
- **6 Validação:** `review`, `security-and-hardening`
- **7 Escrita:** `deep-research`, `docx`/`pdf`, `dataviz`
