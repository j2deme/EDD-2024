from rich.console import Console
from rich.panel import Panel

console = Console()

panel1 = Panel("Hola")
panel2 = Panel.fit("Hola mundo!")

panel3 = Panel("[green]Hola[/green] [blue]mundo[/blue]",
               title="Panel 3", border_style="#ffa500", subtitle="Texto adicional")

console.print(panel1)
console.print(panel2)
console.print(panel3)
print("Hola")
