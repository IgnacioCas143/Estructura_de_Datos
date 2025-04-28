
def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def seleccion(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


entrada = input("Ingrese los números separados por espacios: ")
numeros = list(map(int, entrada.split()))


lista_burbuja = numeros.copy()
burbuja(lista_burbuja)
print("Ordenado por Burbuja:", lista_burbuja)

lista_insercion = numeros.copy()
insercion(lista_insercion)
print("Ordenado por Inserción:", lista_insercion)

lista_seleccion = numeros.copy()
seleccion(lista_seleccion)
print("Ordenado por Selección:", lista_seleccion)
