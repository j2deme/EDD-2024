from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Alumnos")
table.add_column("Número de control", style="green")
table.add_column("Nombre")
table.add_column("Edad", style="blue")

table.add_row("22690316", "Daniel", "21")
table.add_row("21690066", "Maricruz", "20")
table.add_row("22690066", "Edrey", "20")

console.print(table)
