def busqueda_secuencial(lista, elemento_a_buscar):

    indices_encontrados = []
    for i in range(len(lista)):
        if lista[i] == elemento_a_buscar:
            indices_encontrados.append(i)
    return indices_encontrados

def busqueda_binaria(lista_ordenada, elemento_a_buscar):

    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista_ordenada[medio] == elemento_a_buscar:
            return medio
        elif lista_ordenada[medio] < elemento_a_buscar:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1

if __name__ == "__main__":
    mi_lista_secuencial = [10, 23, 4, 56, 7, 82, 19, 45, 7, 30, 7] 
    mi_lista_binaria = sorted(list(set(mi_lista_secuencial))) 

    print("Lista para búsqueda secuencial (puede estar desordenada):", mi_lista_secuencial)
    print("Lista para búsqueda binaria (ordenada):", mi_lista_binaria)
    print("-" * 70)

    try:
        numero_str = input("Ingresa el número que deseas buscar: ")
        numero_a_buscar = int(numero_str)

        print("\n--- Resultados de la Búsqueda ---")


        indices_sec = busqueda_secuencial(mi_lista_secuencial, numero_a_buscar)
        if indices_sec: 
            print(f"Búsqueda Secuencial: El número {numero_a_buscar} SÍ se encuentra en los siguientes índices de la lista original: {indices_sec}.")
        else:
            print(f"Búsqueda Secuencial: El número {numero_a_buscar} NO se encuentra en la lista original.")


        indice_bin = busqueda_binaria(mi_lista_binaria, numero_a_buscar)
        if indice_bin != -1:
            print(f"Búsqueda Binaria: El número {numero_a_buscar} SÍ se encuentra en el índice {indice_bin} de la lista ordenada (sin duplicados en este caso).")
        else:
            print(f"Búsqueda Binaria: El número {numero_a_buscar} NO se encuentra en la lista ordenada (sin duplicados en este caso).")

    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    print("-" * 70)
