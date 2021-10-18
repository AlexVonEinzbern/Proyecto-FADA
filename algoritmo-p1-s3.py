
import numpy as np

from utils.file import read_file, write_output_file
from utils.sort_algorithms import merge_sort
from utils.utils import *

# Variable global
hours_allowed = 24

# Funciones

'''
Maximizar Horas
Selección de actividades que maximicen el total de horas.
La capacidad o disponiblidad está dada por la hora de finalización.
El beneficio está dado por el total de horas que dura una actividad.
'''
def select_tasks_dynamic(datos, order_by):
    # Ordenar las tareas
    task = merge_sort(datos, order_by, less_equal_than)
    # print(task)
    # Cantidad de tareas
    N = len(task)

    # Cantidad de horas disponibles
    M = hours_allowed

    # Insertar elemento vacío en la posición 0
    task.insert(0, {
            'id': 0,
            'nombre': '',
            'hora_i': 0,
            'hora_f': 0,
            'hora_t': 0
        })

    # Se crean las matrices Max y Aux
    b_max, b_aux = createArrays(M, N, task)

    # Total de horas maximizadas
    total_h = int(b_max[M][N])

    # Indices correspondientes a las tareas seleccionadas
    solution = solutionAux(b_aux, M, N, task)

    # Ubicar las tareas seleccionadas
    task_selected = []
    for i in range(1, (N+1)):
        if i in solution:
            task_selected.append(task[i])

    return task_selected, total_h

def createArrays(M, N, task):

    b_max = np.zeros(((M+1), (N+1)))
    b_aux = np.zeros(((M+1), (N+1)))
    habilitado = 0 # Hora inicio disponibilidad

    for j in range(N+1): # Objetos
        for i in range(M+1): # Capacidad
            # print(f'[{i},{j}]')
            W = task[j]['hora_f']
            I = task[j]['hora_i']
            B = task[j]['hora_t']

            if i == 0 or j == 0 :
                b_max[i][j] = 0
                b_aux[i][j] = 0
            elif i >= W:
                # print('i: ', i, ' W: ', W, ' I: ', I, ' habilitado: ', habilitado)
                if (b_max[(i - W)][(j-1)] + B) >= b_max[i][(j-1)] and task[j]['hora_i'] >= task[j-1]['hora_f']:
                    # print(f'SI [{i},{j}]  if {b_max[i][(j-1)]} >= b_max[{(i - W)}][{(j-1)}] => {b_max[(i - W)][(j-1)]} + {B}')
                    b_max[i][j] = (b_max[(i - W)][(j-1)] + B)
                    b_aux[i][j] = 1
                    habilitado = W
                else:
                    # print(f'NO [{i},{j}]  if {b_max[i][(j-1)]} >= b_max[{(i - W)}][{(j-1)}] => {b_max[(i - W)][(j-1)]} + {B}')
                    b_max[i][j] = b_max[i][(j - 1)]
                    b_aux[i][j] = 0
            else:
                b_max[i][j] = b_max[i][(j - 1)]
                b_aux[i][j] = 0

    return b_max, b_aux

def solutionAux(b_aux, i, j, task, resultado=[]):

    W = task[j]['hora_f']

    if i == 0 or j == 0 :
        next
    elif b_aux[i][j] == 1 :
        # print(f'La tarea {j} fue seleccionada')
        resultado.append(j)
        solutionAux(b_aux, (i - W), (j - 1), task, resultado)
    else:
        # print(f'La tarea {j} No fue seleccionada')
        solutionAux(b_aux, i, (j - 1), task, resultado)

    return resultado


if __name__ == '__main__':

    data = read_file()
    task, total_h = select_tasks_dynamic(data, 'hora_f')
    write_output_file(total_h, task)
        