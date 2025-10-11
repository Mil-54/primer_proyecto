# generador.py
import random # Importamos la librería para elegir al azar

def saludar(nombre):
  """Esta función genera un saludo personalizado y aleatorio."""
  saludos_posibles = [
      f"¡Qué bueno verte, {nombre}!",
      f"¡Hola, {nombre}! Bienvenido al mundo de Git y Python.",
      f"¡Un saludo, {nombre}! Programar es un placer."
  ]
  saludo_elegido = random.choice(saludos_posibles)
  print(saludo_elegido)

# Le pedimos al usuario que ingrese un nombre
nombre_usuario = input("Por favor, introduce tu nombre: ")

# Llamamos a la función para mostrar el saludo
saludar(nombre_usuario)
