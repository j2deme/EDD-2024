class NodoBinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        if self.izquierdo is not None and self.derecho is not None:
            return f'({self.izquierdo} <- {self.valor} -> {self.derecho})'
        elif self.izquierdo is not None:
            return f'({self.izquierdo} <- {self.valor})'
        elif self.derecho is not None:
            return f'({self.valor} -> {self.derecho})'
        else:
            return str(self.valor)
