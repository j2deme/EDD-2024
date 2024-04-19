from listaDoble import ListaDoble


class ListaDobleCircular(ListaDoble):
    def __init__(self):
        super().__init__()

    def agregar_final(self, valor):
        super().agregar_final(valor)
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola

    def agregar_inicio(self, valor):
        super().agregar_inicio(valor)
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza

    def recorrer_inicio(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=' -> ' if actual.siguiente else '\n')
            actual = actual.siguiente
            if actual == self.cabeza:
                print()
                break

    def recorrer_fin(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=' -> ' if actual.anterior else '\n')
            actual = actual.anterior
            if actual == self.cola:
                print()
                break

    def recorrer(self, pasos=1):
        actual = self.cabeza
        for _ in range(pasos):
            print(actual.valor, end=" -> ")
            actual = actual.siguiente

    def eliminar_inicio(self):
        if self.cabeza is None:
            return False

        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza

        self.tamanio -= 1
        return True

    def eliminar_final(self):
        if self.cola is None:
            False

        if self.cola.anterior == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior  # Apuntamos al penúltimo
            self.cola.siguiente = self.cabeza  # Penúltimo a cabeza
            self.cabeza.anterior = self.cola  # Cabeza a penúltimo

        self.tamanio -= 1
        return True
