import ntpath
import os
import sys
# Variable global

# Funciones
def leer_archivo():
    ruta_archivo = sys.argv[1]
    f = open (ruta_archivo,'r')
    lineas = f.readlines()
    n = lineas[0]
    datos = []
    for i in range(len(lineas)):
        if i > 0:
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


def insertionSort(array, ordenar_por, func):
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0 and func(key[ordenar_por], array[i][ordenar_por])):
            array[i + 1] = array[i]
            i = i - 1
        array[i+1] = key
    return array

def merge_sort(arr, ordenar_por, func):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left, right = merge_sort(arr[:mid], ordenar_por, func), merge_sort(arr[mid:], ordenar_por, func)

    return merge(left, right, arr.copy(), ordenar_por, func)


def merge(left, right, merged, ordenar_por, func):
    
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        if func(left[left_cursor][ordenar_por], right[right_cursor][ordenar_por]):
            merged[left_cursor + right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

def menor_igual_que(x, y):
    return x <= y

def mayor_que(x, y):
    return x > y

def print_tasks(tasks):
    texto = ""
    for task in tasks:
        nombre = task['nombre']
        hora_i = task['hora_i']
        hora_f = task['hora_f']
        texto += f'{nombre}, {hora_i}, {hora_f} \n'
    print(texto)

def total_hours(data):
    total_h = 0

    for task in data:
        total_h+=task['hora_f']-task['hora_i']
    return total_h

def select_tasks_voraz(datos, value_i, value_f):
    task = []
    orden = merge_sort(datos, value_f, menor_igual_que)
    N = len(orden)
    hora_f = orden[0][value_f]
    task.append(orden[0])
    for i in range(1, N):
        if hora_f<=orden[i][value_i]:
            task.append(orden[i])
            hora_f = orden[i][value_f]
    return task

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


if __name__ == '__main__':

    datos = leer_archivo()
    act = select_tasks_voraz(datos, 'hora_i', 'hora_f')
    total_h = total_hours(act)
    write_output_file(total_h, act)
        