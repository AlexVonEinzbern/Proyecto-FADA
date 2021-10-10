# Variable global
horas_permitidas = 24

# Funciones
def leer_archivo():
    ruta_archivo = input('Ingrese ruta del archivo (ej: data/input.txt): ')
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
            merged[left_cursor+right_cursor]=left[left_cursor]
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

def ordenarDatosDesc(datos):
    ordenados = merge_sort(datos, 'hora_t', mayor_que)
    return ordenados


def ordenarDatosAsc(datos):
    ordenados = merge_sort(datos, 'hora_i', menor_igual_que)
    return ordenados

'''
Verificar que no se crucen tareas
'''
def comparador (seleccionados, tarea_evaluar):
    seleccionar = True
    for tarea in seleccionados:
        # print(tarea_evaluar['hora_f'], ' > ', tarea['hora_i'], ' and ', tarea_evaluar['hora_i'], '<', tarea['hora_f'])
        if tarea_evaluar['hora_f'] > tarea['hora_i'] and tarea_evaluar['hora_i'] < tarea['hora_f']:
            seleccionar = False
    return seleccionar

def maximizarHoras(datos):
    ordenados = ordenarDatosDesc(datos)
    seleccionados = []
    # print('ordenados: ', ordenados)
    suma_horas = 0
    for i in range(len(ordenados)):
 
        actual = ordenados[i]
        if (suma_horas <= horas_permitidas) and (i == 0 or comparador(seleccionados, actual)):
            actual['aplica'] = True
            seleccionados.append(actual)
            suma_horas += actual['hora_t']
        else:
            actual['aplica'] = False
    # print('seleccionados: ', seleccionados)
    return ordenados


def selccionarTareas(datos):
    verificados = maximizarHoras(datos)
    seleccionados = []
    for tarea in verificados:
        if tarea['aplica']:
            seleccionados.append(tarea)
    resultado = ordenarDatosAsc(seleccionados)
    print(f'Se seleccionan tareas')
    return resultado


def horasAutomatizadas(tareas):
    horas = 0
    for tarea in tareas:
        horas += tarea['hora_t']
    return horas


def archivoSalida(tareas):
    ruta = 'data/output.txt'
    f = open (ruta,'w')
    cantidad = len(tareas)
    horas_automatizadas = horasAutomatizadas(tareas)
    texto = f'{cantidad}\n'
    texto += f'{horas_automatizadas}\n'
    for tarea in tareas:
        nombre = tarea['nombre']
        hora_i = tarea['hora_i']
        hora_f = tarea['hora_f']
        texto += f'{nombre}, {hora_i}, {hora_f} \n'

    f.write(texto)
    f.close()
    print(f'Se escribe resultado en el archivo {ruta}')


def principal():
    datos = leer_archivo()
    seleccionados = selccionarTareas(datos)
    archivoSalida(seleccionados)


if __name__ == '__main__':
    #Ejecucion
    principal()
        