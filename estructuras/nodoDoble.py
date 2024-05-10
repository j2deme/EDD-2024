class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

        self.izquierdo = self.siguiente
        self.derecho = self.anterior

    def __str__(self):
        return str(self.valor)
