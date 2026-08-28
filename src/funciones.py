"""
funciones.py

Funciones reutilizables para el análisis de datos del taller de mecatrónica.
"""


def convertir_a_float(valor):
    """
    Intenta convertir un valor a número decimal.
    Retorna el número convertido, o None si el valor no se puede convertir.
    """
    try:
        return float(valor)
    except:
        return None


def calcular_potencia(voltaje, corriente):
    """
    Calcula la potencia a partir de voltaje y corriente.
    Retorna None si voltaje o corriente son None o negativos.
    """
    if voltaje is None or corriente is None:
        return None

    if voltaje < 0 or corriente < 0:
        return None

    return voltaje * corriente


def clasificar_temperatura(temp):
    """
    Clasifica una temperatura según su valor:
    - None -> "Dato inválido"
    - < 40 -> "Normal"
    - 40 a 49.9 -> "Precaución"
    - >= 50 -> "Alerta"
    """
    if temp is None:
        return "Dato inválido"
    elif temp < 40:
        return "Normal"
    elif temp < 50:
        return "Precaución"
    else:
        return "Alerta"


def generar_resumen(registros):
    """
    Genera un resumen estadístico a partir de una lista de registros limpios.
    """
    total_registros = len(registros)

    potencias = [r['potencia'] for r in registros if r['potencia'] is not None]
    temperaturas = [r['temperatura'] for r in registros if r['temperatura'] is not None]

    registros_validos_potencia = len(potencias)
    potencia_promedio = sum(potencias) / len(potencias) if potencias else None
    temperatura_promedio = sum(temperaturas) / len(temperaturas) if temperaturas else None

    cantidad_alertas = len([r for r in registros if r['estado_temperatura'] == 'Alerta'])
    cantidad_precauciones = len([r for r in registros if r['estado_temperatura'] == 'Precaución'])
    cantidad_normales = len([r for r in registros if r['estado_temperatura'] == 'Normal'])

    return {
        'total_registros': total_registros,
        'registros_validos_potencia': registros_validos_potencia,
        'potencia_promedio': potencia_promedio,
        'temperatura_promedio': temperatura_promedio,
        'cantidad_alertas': cantidad_alertas,
        'cantidad_precauciones': cantidad_precauciones,
        'cantidad_normales': cantidad_normales
    }
