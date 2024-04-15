from listaDoble import ListaDoble


class ListaDobleCircular(ListaDoble):
    def __init__(self):
        super().__init__()

    def agregar_final(self, valor):
        super().agregar_final(valor)
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola
