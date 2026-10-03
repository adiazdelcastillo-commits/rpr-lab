import pytest
from calculator.stats import resumen


def test_resumen_basico():
    r = resumen([2, 4, 4, 4, 5, 5, 7, 9])   # datos canonicos de la referencia
    assert r["n"] == 8
    assert r["media"] == 5.0
    assert r["mediana"] == 4.5
    assert r["desviacion"] == 2.0


def test_resumen_un_solo_valor():
    r = resumen([7])
    assert r["n"] == 1
    assert r["media"] == 7.0
    assert r["mediana"] == 7
    assert r["desviacion"] == 0.0     # no se puede desviar con una muestra


def test_requiere_al_menos_un_valor():
    with pytest.raises(ValueError):
        resumen([])