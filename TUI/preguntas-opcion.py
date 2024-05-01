import questionary
from rich.console import Console
from rich import print

Console().clear()  # Limpia la consola

nombre = questionary.text("¿Cuál es tu nombre?", default="Jaime").ask()
color = questionary.select("¿Cuál es tu color favorito?", choices=[
                           "Red", "Green", "Blue", "Otro"], pointer="😎").ask()

if color == "Otro":
    color = questionary.text("¿Cuál es tu color favorito?").ask()

imprimir = questionary.confirm(
    "¿Quieres imprimir el resultado?").ask()

if imprimir:
    print(f"Hola, {nombre}! Tu color favorito es [{color.lower()}]{color}[/].")
else:
    print("Gracias por participar!")
