"""Estadisticas basicas con validacion de entrada."""
from statistics import mean, median, pstdev


def resumen(valores) -> dict:
    datos = [float(v) for v in valores]
    if not datos:
        raise ValueError("se requiere al menos un valor")
    return {
        "n": len(datos),
        "media": round(mean(datos), 6),
        "mediana": median(datos),
        "desviacion": round(pstdev(datos), 6) if len(datos) > 1 else 0.0,
    }