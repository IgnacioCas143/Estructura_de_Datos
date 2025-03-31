from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1  
        self.valores = []
        self.hijos = [] 


class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if not nodo.izquierda:
            nodo.izquierda = Nodo(valor)
        elif not nodo.derecha:
            nodo.derecha = Nodo(valor)
        else:
            self._insertar_recursivo(nodo.izquierda, valor)

    def altura(self):
        return self._altura_recursiva(self.raiz)
    
    def _altura_recursiva(self, nodo):
        if not nodo:
            return 0
        return 1 + max(self._altura_recursiva(nodo.izquierda), self._altura_recursiva(nodo.derecha))
    
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)
    
    def _contar_nodos_recursivo(self, nodo):
        if not nodo:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izquierda) + self._contar_nodos_recursivo(nodo.derecha)
    
    def bfs(self):
        if not self.raiz:
            return
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            print(nodo.valor, end=" ")
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
    

class BST(ArbolBinario):
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self.raiz = self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if not nodo:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo
    
    def encontrar_minimo(self):
        nodo = self.raiz
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.valor
    
    def encontrar_maximo(self):
        nodo = self.raiz
        while nodo.derecha:
            nodo = nodo.derecha
        return nodo.valor
    
class AVL(BST):
    def _altura(self, nodo):
        return nodo.altura if nodo else 0
    
    def _balance_factor(self, nodo):
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)
    
    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        return x
    
    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        return y
    
    def _balancear(self, nodo):
        balance = self._balance_factor(nodo)
        if balance > 1:
            if self._balance_factor(nodo.izquierda) < 0:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1:
            if self._balance_factor(nodo.derecha) > 0:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)
        return nodo
    
    def _insertar_recursivo(self, nodo, valor):
        nodo = super()._insertar_recursivo(nodo, valor)
        return self._balancear(nodo)
    
    
class NodoB:
    def __init__(self, t, hoja=True):
        self.t = t  
        self.hoja = hoja  
        self.claves = []  
        self.hijos = []  

class BTree:
    def __init__(self, t=2):
        self.t = t  
        self.raiz = NodoB(t, hoja=True)  

    def insertar(self, valor):
        raiz = self.raiz
        if len(raiz.claves) == (2 * self.t) - 1:
            nueva_raiz = NodoB(self.t, hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self._dividir(nueva_raiz, 0, self.raiz)
            self.raiz = nueva_raiz
        self._insertar_no_lleno(self.raiz, valor)

    def _insertar_no_lleno(self, nodo, valor):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and valor < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = valor
        else:
            while i >= 0 and valor < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.t) - 1:
                self._dividir(nodo, i, nodo.hijos[i])
                if valor > nodo.claves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], valor)

    def _dividir(self, padre, i, nodo):
        t = self.t
        nuevo_nodo = NodoB(t, hoja=nodo.hoja)
        padre.claves.insert(i, nodo.claves[t - 1])
        padre.hijos.insert(i + 1, nuevo_nodo)
        nuevo_nodo.claves = nodo.claves[t:]
        nodo.claves = nodo.claves[:t - 1]
        if not nodo.hoja:
            nuevo_nodo.hijos = nodo.hijos[t:]
            nodo.hijos = nodo.hijos[:t]

    def buscar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz
        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and valor == nodo.claves[i]:
            return True
        if nodo.hoja:
            return False
        return self.buscar(valor, nodo.hijos[i])

    def recorrer(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        for i in range(len(nodo.claves)):
            if not nodo.hoja:
                self.recorrer(nodo.hijos[i])
            print(nodo.claves[i], end=" ")
        if not nodo.hoja:
            self.recorrer(nodo.hijos[-1])


print("\nÁrbol Binario:")
arbol_binario = ArbolBinario()
arbol_binario.insertar(10)
arbol_binario.insertar(20)
arbol_binario.insertar(30)
arbol_binario.insertar(40)
print("Altura del árbol binario:", arbol_binario.altura())
print("Número de nodos en el árbol binario:", arbol_binario.contar_nodos())
print("Recorrido BFS del árbol binario:")
arbol_binario.bfs()

print("\n\nÁrbol BST:")
arbol_bst = BST()
arbol_bst.insertar(50)
arbol_bst.insertar(30)
arbol_bst.insertar(70)
print("Mínimo en BST:", arbol_bst.encontrar_minimo())
print("Máximo en BST:", arbol_bst.encontrar_maximo())

print("\n\nÁrbol AVL:")
arbol_avl = AVL()
arbol_avl.insertar(50)
arbol_avl.insertar(30)
arbol_avl.insertar(70)
print("Altura del árbol AVL:", arbol_avl.altura())

print("\n\nÁrbol B:")
arbol_b = BTree(t=3)
for v in [10, 20, 5, 6, 12, 30, 7, 17]:
    arbol_b.insertar(v)

print("Recorrido in-order del B-Tree:")
arbol_b.recorrer()
print("\nBuscar 12:", arbol_b.buscar(12))
print("Buscar 25:", arbol_b.buscar(25))
