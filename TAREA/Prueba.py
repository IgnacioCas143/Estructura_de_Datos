from Sorting_Algoritmos import mezcla_equilibrada_k_vias, menu_principal, shell_sort, heap_sort
# Listas ordenadas que quieres usar
sublista1 = [1, 5, 9, 12]
sublista2 = [2, 6, 10, 13]
sublista3 = [3, 7, 11, 14]
sublista4 = [4, 8, 15, 16]

lista_de_listas = [sublista1, sublista2, sublista3, sublista4]

print("-" * 30)
print(f"{mezcla_equilibrada_k_vias(lista_de_listas)}")
print("-" * 30)

# Llamada a la función menu_principal
print("Llamando a menu_principal...")
print(f'{heap_sort(sublista1)}')