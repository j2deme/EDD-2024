from rich import print
from rich.tree import Tree

arbol = Tree("Raíz")
arbol.add("Hijo 1")
arbol.add("[red]Hijo 2")
rama = arbol.add("Hijo 3")
rama.add("Hijo 3.1")
rama2 = rama.add("[blue]Hijo 3.2")
rama2.add("Hijo 3.2.1")

print(arbol)
