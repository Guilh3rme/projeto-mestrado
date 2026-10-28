# Fase 0 — Literatura (levantamento inicial)

> Baseado em resumos de busca, **não em leitura dos artigos**. Verificar cada item antes de citar.

## Associação pessoa↔EPI (existe; a lacuna não é "associar")
- [PPE compliance com detecção + pose (Autom. Constr., 2025)](https://www.sciencedirect.com/science/article/pii/S0926580525002717): detecta EPI e refina o pareamento com ViTPose.
- [TCSS-Net (Frontiers, 2026)](https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2026.1878141/full): grafo topológico do corpo (cabeça, torso, mãos, pés); sem topologia é a pior variante. Obra subterrânea.
- [Scene graph, trabalho em altura (2026)](https://www.sciencedirect.com/science/article/abs/pii/S1474034626003046) e [zero-shot por captioning (2024)](https://www.sciencedirect.com/science/article/abs/pii/S0926580524002061).
- Implicação: nossas zonas por altura são um baseline simples; comparar com pose/grafo. Sem anotação própria, o temporal sai do escopo: contribuição = comparação controlada de associação com F1 por pessoa + robustez + borda (novidade limitada, assumido).

## Datasets
| Dataset | Domínio | Nota |
|---|---|---|
| [SH17](https://github.com/ahmadmughees/SH17dataset) | manufatura, 8.099 img, 17 cls | CC BY-NC-SA 4.0; imagens do Pexels |
| minersPPE | mineração, 8.585 img, 14 cls | frames, sem ID; **licença/acesso a confirmar** |
| CUMT-Helmet / CMUID | mina de carvão | download não confirmado |
| CHV, Construction-PPE (Ultralytics) | construção | fallback, pequenos |
- Nenhum com vídeo + ID de pessoa achado; decisão: sem anotação própria, verdade por pessoa derivada das caixas.

## Robustez a domínio
- [NST-YOLOv5](https://arxiv.org/pdf/2307.13654): style transfer p/ baixa luz, poeira, névoa; +0,083 mAP50:95 em dados reais.
- [Augmentation física (Buildings, 2026)](https://www.citedrive.com/en/discovery/reliable-vision-based-ppe-detection-for-construction-safety-in-adverse-environmental-conditions/): baixa luz mAP50 73,4→87,9%.
- [CLAHE > EnlightenGAN](https://etasr.com/index.php/ETASR/article/view/14254): realce simples como mitigação de baixo custo (E5).
- Mineração: trabalhos single-dataset, foco em objeto pequeno; LODO entre sites pouco estudado.

## Borda
- Sem números INT8/Jetson para EPI achados; [Jetson Nano 12,83 FPS (2022)](https://journal15.magtechjournal.com/Jwk_dlxyzk/CN/Y2022/V7/I12/37), precisão não informada.

## A fazer
- Busca em Scholar/Scopus: "PPE compliance" + tracking/temporal; leitura completa dos 4 artigos de associação.
- Confirmar acesso/licença do minersPPE e CUMT-Helmet.
