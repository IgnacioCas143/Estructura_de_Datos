import heapq # Usaremos un min-heap para hacer la mezcla k-vías eficientemente

def mezcla_equilibrada_k_vias(lista_de_listas_ordenadas):
    
    resultado = []
    min_heap = []

    for i, sublista in enumerate(lista_de_listas_ordenadas):
        if sublista: 
            heapq.heappush(min_heap, (sublista[0], i, 0))


    while min_heap:

        valor, indice_lista, indice_elemento = heapq.heappop(min_heap)
        resultado.append(valor)


        indice_siguiente_elemento = indice_elemento + 1
        if indice_siguiente_elemento < len(lista_de_listas_ordenadas[indice_lista]):
            siguiente_valor = lista_de_listas_ordenadas[indice_lista][indice_siguiente_elemento]
            heapq.heappush(min_heap, (siguiente_valor, indice_lista, indice_siguiente_elemento))
            
    return resultado


if __name__ == "__main__":

    sublista1 = [1, 5, 9, 12]
    sublista2 = [2, 6, 10, 13]
    sublista3 = [3, 7, 11, 14]
    sublista4 = [4, 8, 15, 16]

    lista_de_listas = [sublista1, sublista2, sublista3, sublista4]
    print(f"Listas ordenadas de entrada: {lista_de_listas}")
    
    lista_final_ordenada = mezcla_equilibrada_k_vias(lista_de_listas)
    print(f"Lista combinada y ordenada (Mezcla Equilibrada K-Vías): {lista_final_ordenada}")

    lista_de_listas_2 = [
        [10, 20, 30],
        [], # Lista vacía
        [15, 25],
        [12, 18, 22, 28]
    ]
    print(f"Listas ordenadas de entrada (ejemplo 2): {lista_de_listas_2}")
    lista_final_ordenada_2 = mezcla_equilibrada_k_vias(lista_de_listas_2)
    print(f"Lista combinada y ordenada (ejemplo 2): {lista_final_ordenada_2}")

    lista_de_listas_3 = [
        [1, 3, 5, 7],
        [2, 4, 6, 8]
    ]
    print(f"Listas ordenadas de entrada (ejemplo 3): {lista_de_listas_3}")
    lista_final_ordenada_3 = mezcla_equilibrada_k_vias(lista_de_listas_3)
    print(f"Lista combinada y ordenada (ejemplo 3): {lista_final_ordenada_3}")
