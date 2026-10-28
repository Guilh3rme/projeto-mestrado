# Plano macro

Cada fase tem um objetivo, entregáveis e um **critério de saída** (a fase só fecha quando ele é atendido).
O plano detalhado de cada fase vai em `docs/fase-N-<nome>.md`.

> Durações são relativas e assumem ~24 meses de mestrado; ajustar quando o cronograma oficial existir.

## Visão geral

| Fase | Nome | Duração | Depende de | Experimentos |
|------|------|---------|------------|--------------|
| 0 | Fundação e escopo | 1–2 meses | — | — |
| 1 | Dados | 3–4 meses | 0 | — |
| 2 | Baseline de detecção | 2 meses | 1 | E1, E2 |
| 3 | Rastreamento e associação por pessoa | 3 meses | 2 | E3 |
| 4 | Robustez a domínio | 3–4 meses | 2, 3 | E4, E5 |
| 5 | Borda | 3 meses | 2 (modelo), 3 (pipeline) | E6 |
| 6 | Validação integrada | 2 meses | 3, 4, 5 | — |
| 7 | Escrita e defesa | 3–4 meses (em paralelo desde a Fase 2) | todas | — |

As fases 4 e 5 podem andar em paralelo depois da Fase 3. Artigos parciais saem ao fim das fases 3, 4 e 5.

---

## Fase 0 — Fundação e escopo
**Objetivo:** fixar o problema, a literatura e o ambiente antes de gastar GPU.
- Revisão sistemática curta: detecção de EPI, associação pessoa-EPI, domain shift, detecção em borda.
- Definir classes, EPIs exigidos por cenário (NR-6) e o que conta como "ausente".
- Definir hardware de borda (modelo de Jetson) e orçamento de latência.
- Ambiente reproduzível (Python 3.12, seeds, versionamento de dados e experimentos).
- Definir orientador/linha de pesquisa e cronograma oficial.

**Entregáveis:** pergunta de pesquisa e hipóteses finais; lista de lacunas da literatura; ambiente funcionando.
**Saída:** pergunta, hipóteses e métricas de sucesso aprovadas pelo orientador.

## Fase 1 — Dados
**Objetivo:** dataset com divisão sem vazamento e domínios rotulados.
- Levantar datasets públicos e verificar licenças; reaproveitar o dataset do TCC (checar direitos de uso).
- Definir o esquema de anotação (pessoa + EPIs; opcional: "sem EPI"; ID de pessoa para vídeo).
- Coleta/anotação complementar nos domínios-alvo (mineração, poeira, baixa luz).
- Divisão por **vídeo/cena** e por **domínio**; documentar proporções e estatísticas por classe.
- Cuidados éticos: privacidade/LGPD, anonimização, aprovação do comitê de ética, se aplicável.

**Entregáveis:** dataset versionado, datasheet (origem, licença, estatísticas), scripts de conversão e split.
**Saída:** split sem vazamento verificado por script; cada imagem com domínio rotulado.

## Fase 2 — Baseline de detecção
**Objetivo:** baseline confiável com números reais (o TCC não reporta métricas no texto).
- E1: re-treinar o baseline do TCC no novo split e fixar mAP50/50-95, P, R por classe.
- E2: comparar famílias/tamanhos (YOLOv8/11 n,s,m e ao menos uma alternativa) em acurácia e latência.
- Protocolo de avaliação fechado: conjunto de teste intocado até a Fase 6.

**Entregáveis:** tabela de baselines, configs de treino versionadas, protocolo de avaliação.
**Saída:** resultados reproduzíveis (3 seeds) e modelo(s) candidato(s) escolhido(s).

## Fase 3 — Rastreamento e associação por pessoa
**Objetivo:** decidir conformidade **por trabalhador**, incluindo ausência.
- Detecção de pessoa + rastreamento (ByteTrack ou similar), com IDs estáveis.
- Associação EPI↔pessoa (zonas do corpo → avaliar alternativas: pose, IoU/containment, aprendida).
- Estado temporal por `track_id` (votação/filtro) para separar oclusão de falta real.
- E3: associação com vs. sem temporal; métrica **por pessoa** (F1 de presença/ausência), não só mAP.
- Anotar um subconjunto de vídeos com verdade por pessoa/EPI/intervalo para avaliar.

**Entregáveis:** módulo `src/ppe` funcional ponta a ponta em vídeo; ground truth por pessoa; análise de erros.
**Saída:** F1 por pessoa medido em vídeos não vistos; primeiro artigo (contribuição de associação).

## Fase 4 — Robustez a domínio
**Objetivo:** quantificar e reduzir a queda de desempenho fora do domínio.
- E4: leave-one-domain-out e corrupções sintéticas (baixa luz, poeira/névoa, ruído, desfoque) com níveis de severidade.
- E5: mitigações (augmentation de domínio, fine-tuning, realce de imagem, adaptação não supervisionada) e comparação com custo.
- Analisar se a queda vem da detecção, do rastreamento ou da associação.

**Entregáveis:** curvas de degradação por severidade; ranking de mitigações; análise de falhas.
**Saída:** mitigação que recupera uma fração definida do F1 perdido (meta fixada na Fase 0); segundo artigo.

## Fase 5 — Borda
**Objetivo:** pipeline completo dentro do orçamento de latência no dispositivo.
- E6: PyTorch → ONNX → TensorRT FP16/INT8 (calibração com dados dos domínios-alvo).
- Medir latência p50/p95, FPS, memória e energia no pipeline inteiro (detector + tracker + associação), não só no detector.
- Trade-off acurácia × latência × consumo; avaliar tamanho de entrada e frame skipping.

**Entregáveis:** benchmark reproduzível no dispositivo; tabela de Pareto; build do pipeline para a borda.
**Saída:** orçamento de latência atendido com perda de F1 abaixo do limite fixado; terceiro artigo.

## Fase 6 — Validação integrada
**Objetivo:** avaliar o sistema final no conjunto de teste intocado.
- Rodar o sistema completo (melhor modelo + associação + mitigação + borda) nos vídeos de teste.
- Se possível, teste em campo ou com vídeos de empresa parceira.
- Estudo de casos de falha; limitações; discussão ética (falsos positivos, vigilância de trabalhadores).

**Entregáveis:** resultados finais, ablações consolidadas, demo em vídeo.
**Saída:** hipóteses confirmadas ou refutadas com evidência.

## Fase 7 — Escrita e defesa
**Objetivo:** dissertação e publicações (esta fase corre em paralelo, começa na Fase 2).
- Capítulos escritos incrementalmente após cada fase; artigos dos marcos 3, 4 e 5.
- Repositório e dataset publicados com documentação.
- Qualificação e defesa conforme o calendário do programa.

**Entregáveis:** dissertação, artigos submetidos, repositório público.

---

## Riscos principais
| Risco | Fase | Mitigação |
|-------|------|-----------|
| Dados insuficientes nos domínios difíceis (mineração) | 1 | Começar parceria/coleta cedo; usar datasets públicos + sintético como fallback |
| Direitos/privacidade sobre imagens | 1 | Checar licenças e LGPD na Fase 0 |
| Ground truth por pessoa é caro de anotar | 3 | Anotar só um subconjunto de vídeos; ferramenta semi-automática |
| Oclusão confunde com "ausência" | 3 | Estado temporal e classe "indeterminado" |
| GPU de 8 GB limita modelos grandes | 2 | Focar em n/s/m; fine-tune com batch menor/AMP |
| Dispositivo de borda indisponível | 5 | Decidir hardware na Fase 0; fallback: simular com restrições/clock na GPU local |
| Dependência de uma só fonte de dados | 4 | Pelo menos 3 domínios distintos para LODO |

## Decisões em aberto (fechar na Fase 0)
1. Qual Jetson e qual orçamento de latência (ms/frame)?
2. Quais EPIs são obrigatórios por cenário?
3. "Ausente" vs. "indeterminado" quando há oclusão?
4. Qual a meta numérica de sucesso para F1 por pessoa e recuperação sob shift?
5. Haverá coleta própria nova ou só dados existentes?
