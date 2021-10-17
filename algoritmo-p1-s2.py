from utils.file import read_file, write_output_file
from utils.sort_algorithms import merge_sort
from utils.utils import *

# Variable global
hours_allowed = 24

# Funciones

'''
Verificar que no se crucen tareas
T=No se cruza, F=Si se cruza
'''
def check_task(seleccionados, tarea_verificar):
    for tarea in seleccionados:
        # print(tarea_verificar['hora_f'], ' > ', tarea['hora_i'], ' and ', tarea_verificar['hora_i'], '<', tarea['hora_f'])
        if tarea_verificar['hora_f'] > tarea['hora_i'] and tarea_verificar['hora_i'] < tarea['hora_f']:
            return False
    return True

'''
Maximizar Horas
Selección por mayor cantidad de horas de duración
'''
def select_tasks_voraz(datos, order_by):
    task = []
    orden = merge_sort(datos, order_by, greater_than)
    # print(orden)
    N = len(orden)
    task.append(orden[0])
    total_h = orden[0]['hora_t']
    for i in range(1, N):
        if check_task(task, orden[i]) and (total_h + orden[i]['hora_t']) <= hours_allowed:
            task.append(orden[i])
            total_h += orden[i]['hora_t']
    return task

if __name__ == '__main__':

    data = read_file()
    task = select_tasks_voraz(data, 'hora_t')
    total_h = total_hours(task)
    write_output_file(total_h, task)
        