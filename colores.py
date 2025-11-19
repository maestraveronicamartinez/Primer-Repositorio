# CBTIS 89
# 3ºB PROGRAMACIÓN MATUTINO
# VERÓNICA MARTÍNEZ ANAYA
# Programa que muestra una Lsita desplegable (ComboBox) con diversas opciones, al seleccionar una 
# se mostrará el resultado en la etiqueta resultado.

import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Elige una opción:")
etiqueta.pack(pady=10)

# Crear lista desplegable (Combobox)
opciones = ["Rojo", "Verde", "Azul", "Amarillo", "Morado"]
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)

# Función que se ejecuta al seleccionar un elemento
def mostrar_seleccion(event):
    seleccion = ComboColores.get()  # Obtiene el valor seleccionado
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

# Asociar evento al seleccionar un elemento
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Aún no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

# Iniciar bucle principal
ventana.mainloop()