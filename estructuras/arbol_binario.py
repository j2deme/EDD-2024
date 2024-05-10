from estructuras.nodo_binario import NodoBinario
from estructuras.cola import Cola


class ArbolBinario:
    # Constructor árbol vacío
    # def __init__(self):
    #    self.raiz = None
    #    self.tamanio = 0

    # Constructor árbol con raíz
    def __init__(self, raiz=None):
        if raiz is None:
            self.raiz = None
            self.tamanio = 0
        else:
            self.raiz = NodoBinario(raiz)
            self.tamanio = 1

    def insertar(self, valor):
        nuevo_nodo = NodoBinario(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self.__insertar(self.raiz, nuevo_nodo)

    def __insertar(self, nodo, nuevo_nodo):
        if nuevo_nodo.valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = nuevo_nodo
            else:
                self.__insertar(nodo.izquierdo, nuevo_nodo)
        else:
            if nodo.derecho is None:
                nodo.derecho = nuevo_nodo
            else:
                self.__insertar(nodo.derecho, nuevo_nodo)

    def eliminar(self, valor):
        if self.raiz is not None:
            self.raiz = self.__eliminar(self.raiz, valor)

    def __eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self.__eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.__eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

    def preorden(self):
        self.__preorden(self.raiz)

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self.__preorden(nodo.izquierdo)
            self.__preorden(nodo.derecho)

    def inorden(self):
        self.__inorden(self.raiz)

    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierdo)
            print(nodo.valor)
            self.__inorden(nodo.derecho)

    def postorden(self):
        self.__postorden(self.raiz)

    def __postorden(self, nodo):
        if nodo is not None:
            self.__postorden(nodo.izquierdo)
            self.__postorden(nodo.derecho)
            print(nodo.valor)

    def buscar(self, valor):
        return self.__buscar(self.raiz, valor)

    def __buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self.__buscar(nodo.izquierdo, valor)
        else:
            return self.__buscar(nodo.derecho, valor)

    def altura(self):
        return self.__altura(self.raiz)

    def __altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.__altura(nodo.izquierdo), self.__altura(nodo.derecho))

    def anchura(self):
        return self.__anchura(self.raiz)

    def __anchura(self, nodo):
        if nodo is None:
            return 0
        return max(self.__anchura(nodo.izquierdo), self.__anchura(nodo.derecho)) + 1

    def __str__(self):
        return str(self.raiz)
