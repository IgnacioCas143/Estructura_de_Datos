class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = []
        self.siguiente = None

class ListaPostres:
    def __init__(self):
        self.cabeza = None

    def mostrar_ingredientes(self, nombre_postre):
        actual = self.cabeza
        while actual and actual.nombre != nombre_postre:
            actual = actual.siguiente
        if actual:
            if actual.ingredientes:
                print(f"Ingredientes del postre {nombre_postre}: {', '.join(actual.ingredientes)}")
            else:
                print(f"El postre {nombre_postre} no tiene ingredientes.")
        else:
            print(f"Error: El postre {nombre_postre} no fue encontrado.")

    def agregar_ingrediente(self, nombre_postre, ingredientes):
        actual = self.cabeza
        while actual and actual.nombre != nombre_postre:
            actual = actual.siguiente
        if actual:
            nuevos_ingredientes = [ing for ing in ingredientes if ing not in actual.ingredientes]
            if nuevos_ingredientes:
                actual.ingredientes.extend(nuevos_ingredientes)
                print(f"Ingredientes agregados a {nombre_postre}: {', '.join(nuevos_ingredientes)}")
            else:
                print(f"Error: Todos los ingredientes ya están en {nombre_postre}.")
        else:
            print(f"Error: El postre {nombre_postre} no fue encontrado.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        actual = self.cabeza
        while actual and actual.nombre != nombre_postre:
            actual = actual.siguiente
        if actual:
            if ingrediente in actual.ingredientes:
                actual.ingredientes.remove(ingrediente)
                print(f"Ingrediente '{ingrediente}' eliminado del postre {nombre_postre}")
            else:
                print(f"Error: El ingrediente '{ingrediente}' no está en {nombre_postre}")
        else:
            print(f"Error: El postre {nombre_postre} no fue encontrado.")

    def alta_postre(self, nombre_postre, ingredientes):
        nuevo = NodoPostre(nombre_postre)
        nuevo.ingredientes = ingredientes
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def baja_postre(self, nombre_postre):
        if not self.cabeza:
            print("Error: No hay postres registrados.")
            return
        if self.cabeza.nombre == nombre_postre:
            self.cabeza = self.cabeza.siguiente
            print(f"Postre {nombre_postre} eliminado con todos sus ingredientes.")
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.nombre != nombre_postre:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            print(f"Postre {nombre_postre} eliminado con todos sus ingredientes.")
        else:
            print(f"Error: El postre {nombre_postre} no fue encontrado.")

    def mostrar_postres(self):
        if not self.cabeza:
            print("No hay postres registrados.")
            return
        actual = self.cabeza
        while actual:
            print(f"Postre: {actual.nombre}, Ingredientes: {', '.join(actual.ingredientes)}")
            actual = actual.siguiente

    def eliminar_duplicados_postres(self):
        if not self.cabeza:
            print("No hay postres registrados.")
            return
        nombres_vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.nombre in nombres_vistos:
                previo.siguiente = actual.siguiente
                print(f"Postre duplicado '{actual.nombre}' eliminado.")
            else:
                nombres_vistos.add(actual.nombre)
                previo = actual
            actual = actual.siguiente

lista_postres = ListaPostres()
lista_postres.alta_postre("Pastel", ["Harina", "Azúcar", "Manteca"])
lista_postres.alta_postre("Flan", ["Huevo", "Leche", "Azúcar"])
lista_postres.alta_postre("Pan", ["Huevo", "Harina"])
lista_postres.alta_postre("Pastel", ["Harina", "Azúcar", "Manteca"])
lista_postres.alta_postre("Pan", ["Huevo", "Harina"])

print("\nLista de postres antes de eliminar duplicados:")
lista_postres.mostrar_postres()

print("\nEliminando duplicados...\n")
lista_postres.eliminar_duplicados_postres()

print("\nLista de postres después de eliminar duplicados:")
lista_postres.mostrar_postres()

lista_postres.mostrar_ingredientes("Pastel")
lista_postres.agregar_ingrediente("Pastel", ["Vainilla", "Huevos"])
lista_postres.mostrar_ingredientes("Pastel")
lista_postres.eliminar_ingrediente("Pastel", "Manteca")
lista_postres.mostrar_ingredientes("Pastel")
lista_postres.baja_postre("Flan")

print("\nLista de postres:")
lista_postres.mostrar_postres()
