import questionary
from rich.console import Console
from rich import print

Console().clear()  # Limpia la consola

nombre = questionary.text("¿Cuál es tu nombre?", default="Jaime").ask()
print(f"Hola, {nombre}!")

edad = questionary.text(
    "¿Cuántos años tendrás al final de este año?").ask()
edad = int(edad)
print(f"Tienes {edad} años.")
anio_actual = 2024
anio_nacimiento = anio_actual - edad
print(f"Naciste en {anio_nacimiento}.")

contrasena = questionary.password("Escribe tu contraseña").ask()
print(f"Tu contraseña tiene {len(contrasena)} caracteres.")
