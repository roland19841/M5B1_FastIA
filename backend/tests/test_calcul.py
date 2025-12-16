from modules.calcul import calcul

def test_calcul_square():
    assert calcul(3) == 9
    assert calcul(0) == 0
    assert calcul(-4) == 16
