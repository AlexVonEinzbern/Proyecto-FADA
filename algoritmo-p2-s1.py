"""
UNIVERSIDAD DEL VALLE
FUNDAMENTOS DE ANÁLISIS Y DISEÑO DE ALGORITMOS | MINI-PROYECTO 
ESTUDIANTES:
MARIO ALEXANDER DÍAZ, COD. 1825106 
LISETH DAYANA CASTILLO QUIÑONES, CÓD. 1843187
"""

import os
import time
from utils.file import read_file, write_output_file
from utils.sort_algorithms import merge_sort
from utils.utils import *

# Variable global
hours_allowed = 24

# Funciones

'''
Maximizar Tareas
Selección por menor a mayor hora final de cada tarea
'''
def select_tasks_voraz(datos, order_by):
    task = []
    orden = merge_sort(datos, order_by, less_equal_than)
    # print(orden)
    N = len(orden)
    hora_f = orden[0]['hora_f']
    task.append(orden[0])
    total_h = orden[0]['hora_t']
    for i in range(1, N):
        if hora_f<=orden[i]['hora_i'] and (total_h + orden[i]['hora_t']) <= hours_allowed:
            task.append(orden[i])
            hora_f = orden[i]['hora_f']
            total_h += orden[i]['hora_t']
    print('Se seleccionan las tareas')
    return task

def robotic():
    with  open(output, 'a') as f:
        # Leer el archivo con las tareas
        data = read_file()

        # Registro de tiempo inicio ejecución
        start_time = time.time()

        # Seleccionar las tareas
        task = select_tasks_voraz(data, 'hora_f')

        # Registro de tiempo fin ejecución
        final_time = time.time()-start_time

        # total de horas
        total_h = total_hours(task)

        # Escribir archivo con el total de horas y tareas seleccionadas
        write_output_file(total_h, task)

        # Escribir tiempo
        f.write(f'{str(final_time)}\n')

if __name__ == '__main__':
    output = 'times/algoritmo-p2-s1_times.txt'
    if not os.path.exists(os.path.dirname(output)):
        try:
            os.makedirs(os.path.dirname(output))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise 
    
    robotic()
        