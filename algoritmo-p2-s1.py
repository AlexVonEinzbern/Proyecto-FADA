from utils.file import leer_archivo, write_output_file
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

    data = leer_archivo()
    task = select_tasks_voraz(data, 'hora_f')
    total_h = total_hours(task)
    write_output_file(total_h, task)
        