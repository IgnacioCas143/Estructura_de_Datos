import networkx as nx
import matplotlib.pyplot as plt
import random

estados = ["Chiapas", "Yucatán", "Tabasco", "Quintana Roo", "Puebla", "Guadalajara", "Guerrero"]
G = nx.Graph()
G.add_nodes_from(estados)

conexiones = [
    ("Chiapas", "Tabasco"),
    ("Chiapas", "Guerrero"),
    ("Tabasco", "Yucatán"),
    ("Tabasco", "Quintana Roo"),
    ("Yucatán", "Quintana Roo"),
    ("Puebla", "Guadalajara"),
    ("Guadalajara", "Guerrero"),
    ("Puebla", "Guerrero"),
    ("Yucatán", "Puebla")
]

for e1, e2 in conexiones:
    costo = random.randint(1, 100)
    G.add_edge(e1, e2, weight=costo)


while not nx.is_connected(G):
    nodo1, nodo2 = random.sample(estados, 2)
    if not G.has_edge(nodo1, nodo2):
        G.add_edge(nodo1, nodo2, weight=random.randint(1, 100))


print(f"g=({G.number_of_nodes()},{G.number_of_edges()})")

def camino_hamiltoniano(graph):
    return list(nx.approximation.traveling_salesman_problem(graph, cycle=False))

def ciclo_hamiltoniano(graph):
    ruta = camino_hamiltoniano(graph)
    if graph.has_edge(ruta[-1], ruta[0]):
        ruta.append(ruta[0])
    else:
        for nodo in ruta:
            if graph.has_edge(ruta[-1], nodo):
                ruta.append(nodo)
                break
    return ruta

ruta1 = camino_hamiltoniano(G)
ruta2 = ciclo_hamiltoniano(G)

print("Recorrido sin repetir (Camino de Hamilton):", ruta1)
print("Recorrido con repetición (Ciclo de Hamilton):", ruta2)

def calcular_costo(graph, ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        if graph.has_edge(ruta[i], ruta[i+1]):
            costo_total += graph[ruta[i]][ruta[i+1]]['weight']
        else:
            print(f"Advertencia: No hay conexión entre {ruta[i]} y {ruta[i+1]} - Ajusta las conexiones del grafo.")
            return None
    return costo_total

costo_ruta1 = calcular_costo(G, ruta1)
costo_ruta2 = calcular_costo(G, ruta2)

if costo_ruta1 is not None:
    print("Costo total del recorrido sin repetir:", costo_ruta1)
if costo_ruta2 is not None:
    print("Costo total del recorrido con repetición:", costo_ruta2)

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de estados y costos de traslado")
plt.show()

