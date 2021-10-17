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
    return task

if __name__ == '__main__':
    output = 'times/algoritmo-p2-s1_times.txt'
    if not os.path.exists(os.path.dirname(output)):
        try:
            os.makedirs(os.path.dirname(output))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise 

    with  open(output, 'a') as f:
        data = read_file()
        start_time = time.time()
        task = select_tasks_voraz(data, 'hora_f')
        final_time = time.time()-start_time
        total_h = total_hours(task)
        write_output_file(total_h, task)
        f.write(f'{str(final_time)}\n')
        