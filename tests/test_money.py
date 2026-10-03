import pytest
from decimal import Decimal
from calculator.money import redondear, total_factura


@pytest.mark.parametrize("monto,esperado", [
    (10.005, "10.01"),
    (2.675,  "2.68"),
    (0,      "0.00"),
])
def test_redondeo_comercial(monto, esperado):
    assert redondear(monto) == Decimal(esperado)


def test_monto_invalido():
    with pytest.raises(ValueError):
        redondear("abc")


def test_decimales_negativos():
    with pytest.raises(ValueError):
        redondear(10, -1)


def test_total_con_impuesto():
    # 10.00 + 5.50 = 15.50;  15.50 * 0.16 = 2.48;  total = 17.98
    assert total_factura([("a", 10.00), ("b", 5.50)]) == Decimal("17.98")