from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar, List
import math
from doctest import testmod

class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...
  

T = TypeVar("T", bound=Comparable)


# 1. ShellSort
def shell_sort(coleccion: MutableSequence[T]) -> None:
    n = len(coleccion)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = coleccion[i]
            j = i
            while j >= intervalo and coleccion[j - intervalo] > temp:
                coleccion[j] = coleccion[j - intervalo]
                j -= intervalo
            coleccion[j] = temp
        intervalo //= 2

# 2. Quicksort
def _particion(coleccion: MutableSequence[T], bajo: int, alto: int) -> int:
    pivote = coleccion[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if coleccion[j] < pivote:
            i += 1
            coleccion[i], coleccion[j] = coleccion[j], coleccion[i]
    coleccion[i + 1], coleccion[alto] = coleccion[alto], coleccion[i + 1]
    return i + 1

def _quick_sort_recursivo(coleccion: MutableSequence[T], bajo: int, alto: int) -> None:
    if bajo < alto:
        pi = _particion(coleccion, bajo, alto)
        _quick_sort_recursivo(coleccion, bajo, pi - 1)
        _quick_sort_recursivo(coleccion, pi + 1, alto)

def quick_sort(coleccion: MutableSequence[T]) -> None:
    _quick_sort_recursivo(coleccion, 0, len(coleccion) - 1)

# 3. Heapsort
def _heapify(coleccion: MutableSequence[T], n: int, i: int) -> None:
    mas_grande = i
    izquierda = 2 * i + 1
    derecha = 2 * i + 2

    if izquierda < n and coleccion[izquierda] > coleccion[mas_grande]:
        mas_grande = izquierda
    if derecha < n and coleccion[derecha] > coleccion[mas_grande]:
        mas_grande = derecha

    if mas_grande != i:
        coleccion[i], coleccion[mas_grande] = coleccion[mas_grande], coleccion[i]
        _heapify(coleccion, n, mas_grande)

def heap_sort(coleccion: MutableSequence[T]) -> None:
    n = len(coleccion)
    if n <= 1:
        return

    for i in range(n // 2 - 1, -1, -1):
        _heapify(coleccion, n, i)

    for i in range(n - 1, 0, -1):
        coleccion[i], coleccion[0] = coleccion[0], coleccion[i]
        _heapify(coleccion, i, 0)

# 4. Radix Sort (para enteros, incluyendo negativos)
def _counting_sort_para_radix(arr: MutableSequence[int], exp: int) -> None:
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def _radix_sort_no_negativos(arr: MutableSequence[int]) -> None:
    if not arr:
        return
    max_val = 0
    for item in arr:
        if item > max_val:
            max_val = item
    
    exp = 1
    while max_val // exp > 0:
        _counting_sort_para_radix(arr, exp)
        exp *= 10

def radix_sort(coleccion: MutableSequence[int]) -> None:
    if not coleccion:
        return

    negativos = [num for num in coleccion if num < 0]
    positivos = [num for num in coleccion if num >= 0]

    lista_negativos_ordenada = []
    if negativos:
        abs_negativos = [abs(num) for num in negativos]
        _radix_sort_no_negativos(abs_negativos)
        lista_negativos_ordenada = [-num for num in reversed(abs_negativos)]
    
    if positivos:
        _radix_sort_no_negativos(positivos) 
    
    coleccion[:] = lista_negativos_ordenada + positivos


# --- Lógica del Menú Interactivo ---
def obtener_numeros_del_usuario() -> List[int]:
    while True:
        entrada_usuario = input("Ingresa los números separados por comas (ej: 5,2,8,1,0,-3):\n").strip()
        if not entrada_usuario:
            print("No se ingresaron números. Intenta de nuevo.")
            continue
        try:
            numeros = [int(item.strip()) for item in entrada_usuario.split(",")]
            return numeros
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números enteros separados por comas.")

def menu_principal():
    while True:
        print("\n--- Menú de Algoritmos de Ordenamiento ---")
        print("1. ShellSort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Por favor, elige un número entre 1 y 5.")
            continue

        numeros_a_ordenar = obtener_numeros_del_usuario()
        
        numeros_originales = list(numeros_a_ordenar)
        
        lista_para_ordenar_ref = numeros_a_ordenar 
        nombre_algoritmo = ""

        if opcion == '1':
            nombre_algoritmo = "ShellSort"
            shell_sort(lista_para_ordenar_ref)
        elif opcion == '2':
            nombre_algoritmo = "Quicksort"
            quick_sort(lista_para_ordenar_ref)
        elif opcion == '3':
            nombre_algoritmo = "Heapsort"
            heap_sort(lista_para_ordenar_ref)
        elif opcion == '4':
            nombre_algoritmo = "Radix Sort"
            radix_sort(lista_para_ordenar_ref)
        
        print("\n--- Resultados ---")
        print(f"Lista original: {numeros_originales}")
        print(f"Lista ordenada con {nombre_algoritmo}: {lista_para_ordenar_ref}")

if __name__ == "__main__":
    resultados_test = testmod()
    print(f"Pruebas intentadas: {resultados_test.attempted}, Pruebas fallidas: {resultados_test.failed}")
    if resultados_test.failed == 0:
        print("¡Todos los doctests pasaron exitosamente!")
    else:
        print("¡Atención! Algunos doctests fallaron.")
    
    menu_principal()
