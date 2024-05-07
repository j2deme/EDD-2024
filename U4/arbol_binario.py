from nodo_binario import NodoBinario


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
