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


def insertionSortDesc(array, ordenar_por):
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0 and (key[ordenar_por] > array[i][ordenar_por])):
            array[i + 1] = array[i]
            i = i - 1
        array[i+1] = key
    return array


def insertionSortAsc(array, ordenar_por):
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while (i >= 0 and (key[ordenar_por] < array[i][ordenar_por])):
            array[i + 1] = array[i]
            i = i - 1
        array[i+1] = key
    return array


def ordenarDatosDesc(datos):
    ordenados = insertionSortDesc(datos, 'hora_t')
    return ordenados


def ordenarDatosAsc(datos):
    ordenados = insertionSortAsc(datos, 'hora_i')
    return ordenados

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


#Ejecucion
principal()