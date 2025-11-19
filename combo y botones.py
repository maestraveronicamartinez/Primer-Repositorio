import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de lista desplegable")
ventana.geometry("400x250")

# Etiqueta de instrucción
label_instruccion = tk.Label(ventana, text="Selecciona una carrera:", font=("Arial", 12))
label_instruccion.pack(pady=10)

# Lista de opciones
opciones = [
    "ARH",
    "Arquitectura",
    "Comercio electrónico",
    "Comercio internacional y aduanas",
    "Construcción",
    "Contabilidad",
    "Mecatrónica",
    "Programación"
]

# Crear lista desplegable (Combobox)
carrera = ttk.Combobox(ventana, values=opciones, state="readonly", font=("Arial", 11))
carrera.pack(pady=5)

# Etiqueta para mostrar la selección
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=15)

# Función para mostrar la selección
def mostrar_seleccion():
    seleccion = carrera.get()
    if seleccion:
        label_resultado.config(text=f"Has seleccionado: {seleccion}")
    else:
        label_resultado.config(text="No has seleccionado ninguna carrera")

# Botones en una fila
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text="Primero", width=10, command=mostrar_seleccion)
boton1.grid(row=0, column=0, padx=5)

boton2 = tk.Button(frame_botones, text="Tercero", width=10, command=mostrar_seleccion)
boton2.grid(row=0, column=1, padx=5)

boton3 = tk.Button(frame_botones, text="Quinto", width=10, command=mostrar_seleccion)
boton3.grid(row=0, column=2, padx=5)

# Iniciar la aplicación
ventana.mainloop()