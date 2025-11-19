import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista desplegable con botones")
ventana.geometry("420x280")

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

# Crear lista desplegable
carrera = ttk.Combobox(ventana, values=opciones, state="readonly", font=("Arial", 11))
carrera.pack(pady=5)

# Etiqueta para mostrar resultados
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
label_resultado.pack(pady=15)

# Funciones para los botones
def accion_primero():
    seleccion = carrera.get()
    if seleccion:
        label_resultado.config(
            text=f"{seleccion} - Has presionado el botón 'Primero'",
            fg="blue"
        )
    else:
        label_resultado.config(text="Por favor, selecciona una carrera primero.", fg="red")

def accion_tercero():
    seleccion = carrera.get()
    if seleccion:
        label_resultado.config(
            text=f"{seleccion} - Has presionado el botón 'Tercero'",
            fg="green"
        )
    else:
        label_resultado.config(text="Por favor, selecciona una carrera primero.", fg="red")

def accion_quinto():
    seleccion = carrera.get()
    if seleccion:
        label_resultado.config(
            text=f"{seleccion} - Has presionado el botón 'Quinto'",
            fg="purple"
        )
    else:
        label_resultado.config(text="Por favor, selecciona una carrera primero.", fg="red")

# Frame para los botones (alineados horizontalmente)
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Crear los botones
boton1 = tk.Button(frame_botones, text="Primero", width=10, command=accion_primero)
boton1.grid(row=0, column=0, padx=5)

boton2 = tk.Button(frame_botones, text="Tercero", width=10, command=accion_tercero)
boton2.grid(row=0, column=1, padx=5)

boton3 = tk.Button(frame_botones, text="Quinto", width=10, command=accion_quinto)
boton3.grid(row=0, column=2, padx=5)

# Iniciar la aplicación
ventana.mainloop()