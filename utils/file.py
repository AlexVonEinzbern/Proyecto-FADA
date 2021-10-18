"""
UNIVERSIDAD DEL VALLE
FUNDAMENTOS DE ANÁLISIS Y DISEÑO DE ALGORITMOS | MINI-PROYECTO 
ESTUDIANTES:
MARIO ALEXANDER DÍAZ, COD. 1825106 
LISETH DAYANA CASTILLO QUIÑONES, CÓD. 1843187
"""

import ntpath
import os
import sys
# Variable global

# Funciones
def read_file():
    ruta_archivo = sys.argv[1]
    f = open (ruta_archivo,'r')
    lineas = f.readlines()
    n = lineas[0]
    datos = []
    for i in range(1, len(lineas)):
        linea = lineas[i].replace('\n','').split(sep=',')
        tarea = linea[0]
        hora_i = int(linea[1])
        hora_f = int(linea[2])
        hora_t = (hora_f - hora_i)
        datos.append({
            'id': i,
            'nombre': tarea,
            'hora_i': hora_i,
            'hora_f': hora_f,
            'hora_t': hora_t
        })
    f.close()
    print(f'Se lee archivo')
    return datos


def write_output_file(hours, tasks, input=sys.argv[1]):
    output = 'output/output-'+ntpath.basename(input)
    if not os.path.exists(os.path.dirname(output)):
        try:
            os.makedirs(os.path.dirname(output))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise 
    with open(output, "w") as f:
        cantidad = len(tasks)
        horas_automatizadas = hours
        texto = f'{cantidad}\n'
        texto += f'{horas_automatizadas}\n'
        for task in tasks:
            nombre = task['nombre']
            hora_i = task['hora_i']
            hora_f = task['hora_f']
            texto += f'{nombre}, {hora_i}, {hora_f} \n'

        f.write(texto)
        f.close()
    print(f'Se escribe resultado en el archivo {output}')