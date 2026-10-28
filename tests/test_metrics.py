from ppe.metrics import presence_f1


def test_f1_por_epi():
    pairs = [({"helmet": True}, {"helmet": True}), ({"helmet": True}, {"helmet": False}),
             ({"helmet": False}, {"helmet": True})]
    p, r, f = presence_f1(pairs)["helmet"]
    assert (p, r, round(f, 3)) == (0.5, 0.5, 0.5)
