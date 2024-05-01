from rich import print
from rich.console import Console
import questionary

console = Console()
console.clear()  # Limpia la consola

tamanio = questionary.select("¿Cuál es el tamaño de tu pizza?", choices=[
                             "Chica", "Mediana", "Grande"]).ask()

ingredientes = questionary.checkbox("¿Qué ingredientes quieres en tu pizza?", choices=["Pepperoni", "Jamón", "Pimiento", "Queso extra"], pointer="🍕"
                                    ).ask()

print(
    f"Tu pizza {tamanio.lower()} con {', '.join(ingredientes)} está en camino!")
