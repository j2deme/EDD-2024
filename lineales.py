from estructuras.nodo import Nodo
from estructuras.listaSimple import ListaSimple
from estructuras.listaDoble import ListaDoble
from estructuras.listaDobleCircular import ListaDobleCircular as ListaCircular
from estructuras.pila import Pila
from estructuras.cola import Cola


def main():
    ejemploCola()


def ejemploListaSimple():
    lista = ListaSimple()

    print("Representación en memoria:", lista)

    lista.agregar(10)
    lista.agregar(30)
    lista.agregar(50)

    print("Cabeza:", lista.cabeza.valor)
    print("Cola:", lista.cola.valor)

    lista.recorrer()

    lista.eliminar(30)
    lista.recorrer()

    print("Buscar 30: ", lista.buscar(30))
    print("Buscar 10: ", lista.buscar(10))


def ejemploListaDoble():
    lista = ListaDoble()
    lista.recorrer_inicio()

    lista.agregar_final(10)  # 10
    lista.agregar_inicio(20)  # 20 <-> 10
    lista.agregar(30)  # 20 <-> 10 <-> 30
    lista.agregar(40)  # 20 <->10 <-> 30 <-> 40
    lista.agregar(50)  # 20 <->10 <-> 30 <-> 40 <-> 50
    lista.recorrer_inicio()
    lista.recorrer_fin()

    print("Eliminaciones")
    lista.eliminar_inicio()  # 10 <-> 30 <-> 40 <-> 50
    lista.recorrer_inicio()
    lista.eliminar_final()  # 10 <-> 30 <-> 40
    lista.recorrer_inicio()
    lista.eliminar(10)  # 30 <-> 40
    lista.recorrer_inicio()

    lista.agregar_inicio(30)
    lista.agregar_inicio(40)
    lista.recorrer_inicio()

    print("Buscar 30:", lista.buscar(30))
    print("Buscar 75:", lista.buscar(75))


def ejemploListaCircular():
    lista = ListaCircular()
    # lista.recorrer_inicio()

    lista.agregar_inicio(100)
    lista.agregar_inicio(200)
    # lista.recorrer_inicio()
    lista.agregar_final(250)
    lista.agregar_inicio(300)
    lista.agregar_final(400)
    print("Elementos de la lista circular")
    lista.recorrer_inicio()
    # lista.recorrer_fin()
    # lista.recorrer(7)
    # print("Eliminaciones")
    # for _ in range(lista.tamanio):
    #    lista.eliminar_final()
    #    lista.recorrer_inicio()
    lista.agregar(500, 2)
    lista.eliminar(5)
    lista.agregar(600, 4)
    lista.eliminar(0)

    lista.recorrer_inicio()


def ejemploPila():
    pila = Pila()
    print("Cima: ", pila.consultar(), pila.tamanio)

    pila.apilar(10)  # 10
    pila.apilar(20)  # 10 -> 20
    pila.apilar(30)  # 10 -> 20 -> 30

    pila.recorrer()
    print("Cima: ", pila.consultar(), pila.tamanio)
    pila.desapilar()
    pila.recorrer()
    print("❌" if pila.esta_vacia() else "✅")

# Ejemplo de cola simple


def ejemploCola():
    cola = Cola()
    print("Tamaño: {}, Frente: {}".format(cola.size(), cola.consultar()))

    cola.encolar("Martín")
    cola.encolar("Mario")
    cola.encolar("Rigo")
    print("Tamaño: {}, Frente: {}".format(cola.size(), cola.consultar()))
    cola.desencolar()
    cola.recorrer_inicio()
    cola.encolar("Dani")
    print("Esta vacía?", "✅" if cola.esta_vacia() else "❌")
    for i in range(cola.size() + 1):
        cola.recorrer_inicio()
        cola.desencolar()


def nodos():
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3


if __name__ == "__main__":
    main()
