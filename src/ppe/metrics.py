"""F1 de presença por pessoa e por EPI."""


def presence_f1(pairs: list) -> dict:
    """pairs: [(pred, gt)], ambos {classe: bool} por pessoa. Retorna {classe: (P, R, F1)}.

    Ausente e presente contam como classes de uma tarefa binária; "positivo" = EPI presente.
    """
    out = {}
    for c in {c for p, _ in pairs for c in p}:
        tp = sum(p[c] and g[c] for p, g in pairs if c in p)
        fp = sum(p[c] and not g[c] for p, g in pairs if c in p)
        fn = sum(not p[c] and g[c] for p, g in pairs if c in p)
        pr = tp / (tp + fp) if tp + fp else 0.0
        rc = tp / (tp + fn) if tp + fn else 0.0
        out[c] = (pr, rc, 2 * pr * rc / (pr + rc) if pr + rc else 0.0)
    return out
