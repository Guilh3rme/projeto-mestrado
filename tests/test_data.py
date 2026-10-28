from ppe.data import remap_label


def test_remap_descarta_e_reindexa():
    src = "0 .5 .5 .1 .1\n16 .4 .4 .2 .2\n3 .1 .1 .1 .1\n14 .9 .9 .1 .1\n"
    assert remap_label(src) == "0 .5 .5 .1 .1\n3 .4 .4 .2 .2\n5 .9 .9 .1 .1\n"
