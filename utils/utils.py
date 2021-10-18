"""
UNIVERSIDAD DEL VALLE
FUNDAMENTOS DE ANÁLISIS Y DISEÑO DE ALGORITMOS | MINI-PROYECTO 
ESTUDIANTES:
MARIO ALEXANDER DÍAZ, COD. 1825106 
LISETH DAYANA CASTILLO QUIÑONES, CÓD. 1843187
"""

def less_equal_than(x, y):
    return x <= y

def greater_than(x, y):
    return x > y

def total_hours(data):
    total_h = 0

    for task in data:
        total_h+=task['hora_t']
    return total_h