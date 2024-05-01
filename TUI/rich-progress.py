from time import sleep
from rich.progress import Progress

with Progress() as barra:
    tarea = barra.add_task("[green]Descargando...", total=100)

    for i in range(100):
        barra.update(tarea, advance=1)
        barra.refresh()
        sleep(0.05)
