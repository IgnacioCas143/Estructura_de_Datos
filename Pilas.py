class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
        if not self.estaVacia():
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)


def cadenaInversa(miCadena):
    pila = Pila() 
    for caracter in miCadena:  
        pila.incluir(caracter) 
    cadena_revertida = ""
    while not pila.estaVacia(): 
        cadena_revertida += pila.extraer() 
    return cadena_revertida

print(cadenaInversa('Casa'))
print(cadenaInversa('123456789'))
