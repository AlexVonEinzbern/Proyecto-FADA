"""
UNIVERSIDAD DEL VALLE
FUNDAMENTOS DE ANÁLISIS Y DISEÑO DE ALGORITMOS | MINI-PROYECTO 
ESTUDIANTES:
MARIO ALEXANDER DÍAZ, COD. 1825106 
LISETH DAYANA CASTILLO QUIÑONES, CÓD. 1843187
"""

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

