"""Calculo monetario con redondeo seguro."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def redondear(monto, decimales: int = 2) -> Decimal:
    """Redondea usando redondeo comercial (half-up), no banker's rounding."""
    try:
        valor = Decimal(str(monto))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Monto invalido: {monto!r}") from exc
    if not isinstance(decimales, int) or decimales < 0:
        raise ValueError("decimales debe ser un entero >= 0")
    return valor.quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP)


def total_factura(items, tasa_impuesto: str = "0.16") -> Decimal:
    """Suma subtotales y aplica impuesto."""
    subtotal = sum((redondear(p) for _, p in items), Decimal("0"))
    return redondear(subtotal + subtotal * Decimal(tasa_impuesto))