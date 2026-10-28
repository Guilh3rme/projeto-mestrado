from ppe.associate import Item, Person, associate

P = Person(1, (100, 0, 200, 400))  # pessoa 100x400


def test_presente_e_ausente():
    items = [Item("helmet", (130, 5, 170, 40)), Item("boots", (110, 350, 190, 395))]
    r = associate(P, items, {"helmet", "vest", "boots"})
    assert r == {"helmet": True, "vest": False, "boots": True}


def test_epi_fora_da_zona_ou_da_pessoa_nao_conta():
    items = [Item("helmet", (130, 300, 170, 340)), Item("vest", (300, 100, 380, 200))]
    r = associate(P, items, {"helmet", "vest"})
    assert r == {"helmet": False, "vest": False}
