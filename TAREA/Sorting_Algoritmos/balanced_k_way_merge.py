import heapq  # Usamos un min-heap para hacer la mezcla k-vías eficientemente

def mezcla_equilibrada_k_vias(lista_de_listas_ordenadas):
    """
    Intercala k listas ordenadas en una sola lista ordenada.
    Utiliza un heap mínimo para mantener eficiencia.
    """
    resultado = []
    min_heap = []

    # Inicializar el heap con el primer elemento de cada lista no vacía
    for i, sublista in enumerate(lista_de_listas_ordenadas):
        if sublista:  # Solo si la sublista no está vacía
            heapq.heappush(min_heap, (sublista[0], i, 0))

    # Mientras el heap no esté vacío, extraer el menor y agregar el siguiente de su sublista
    while min_heap:
        valor, indice_lista, indice_elemento = heapq.heappop(min_heap)
        resultado.append(valor)

        siguiente_indice = indice_elemento + 1
        if siguiente_indice < len(lista_de_listas_ordenadas[indice_lista]):
            siguiente_valor = lista_de_listas_ordenadas[indice_lista][siguiente_indice]
            heapq.heappush(min_heap, (siguiente_valor, indice_lista, siguiente_indice))

    return resultado


# Ejecución de pruebas
if __name__ == "__main__":
    print("=== Ejemplo 1 ===")
    listas1 = [
        [1, 5, 9, 12],
        [2, 6, 10, 13],
        [3, 7, 11, 14],
        [4, 8, 15, 16]
    ]
    print("Listas ordenadas de entrada:", listas1)
    resultado1 = mezcla_equilibrada_k_vias(listas1)
    print("Lista final ordenada:", resultado1)

    print("\n=== Ejemplo 2 (con listas vacías y tamaños irregulares) ===")
    listas2 = [
        [10, 20, 30],
        [],
        [15, 25],
        [12, 18, 22, 28]
    ]
    print("Listas ordenadas de entrada:", listas2)
    resultado2 = mezcla_equilibrada_k_vias(listas2)
    print("Lista final ordenada:", resultado2)

    print("\n=== Ejemplo 3 (similar a mezcla de Merge Sort) ===")
    listas3 = [
        [1, 3, 5, 7],
        [2, 4, 6, 8]
    ]
    print("Listas ordenadas de entrada:", listas3)
    resultado3 = mezcla_equilibrada_k_vias(listas3)
    print("Lista final ordenada:", resultado3)
