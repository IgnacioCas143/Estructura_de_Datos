class Pila:
    def __init__(self, capacidad=8):
        self.pila = []
        self.capacidad = capacidad
    
    def insertar(self, elemento):
        if len(self.pila) < self.capacidad:
            self.pila.append(elemento)
            print(f"Insertado: {elemento}  -> Pila: {self.pila}")
        else:
            print("❌ Error: Desbordamiento (Overflow), la pila está llena.")
    
    def eliminar(self):
        if len(self.pila) > 0:
            eliminado = self.pila.pop()
            print(f"Eliminado: {eliminado}  -> Pila: {self.pila}")
        else:
            print("Error: Subdesbordamiento (Underflow), la pila está vacía.")

# Simulación
def main():
    pila = Pila()
    
    operaciones = [
        ("insertar", "X"),
        ("insertar", "Y"),
        ("eliminar", None),  # Eliminar (Z) -> Se elimina el tope (Y)
        ("eliminar", None),  # Eliminar (T) -> Se elimina el tope (X)
        ("eliminar", None),  # Eliminar (U) -> Error, pila vacía
        ("insertar", "V"),
        ("insertar", "W"),
        ("eliminar", None),  # Eliminar (p) -> Se elimina el tope (W)
        ("insertar", "R")
    ]
    
    for operacion, valor in operaciones:
        if operacion == "insertar":
            pila.insertar(valor)
        elif operacion == "eliminar":
            pila.eliminar()
    
    print("\n Resultado final de la pila:", pila.pila)
    print(f"La pila quedó con {len(pila.pila)} elementos.")

if __name__ == "__main__":
    main()
