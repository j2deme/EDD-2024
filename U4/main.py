from arbol_binario import ArbolBinario


def main():
    ejemploArbolBinario()


def ejemploArbolBinario():
    arbolVacio = ArbolBinario()
    arbolRaiz = ArbolBinario(10)

    arbolVacio.insertar(5)
    arbolVacio.insertar(7)

    arbolRaiz.insertar(5)
    arbolRaiz.insertar(15)


if __name__ == "__main__":
    main()
