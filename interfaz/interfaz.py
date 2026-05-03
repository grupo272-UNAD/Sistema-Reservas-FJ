#Karen Marcela Chara Mina
# Fase 4 


#Importamos la biblioteca tkinter para crear la interface
#Importamos el módulo messagebox de tkinter para mostrar mensajes emergentes

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

# FUNCIONES DE VALIDACION

def registrar_cliente():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    identificacion = entry_identificacion.get()

    if nombre == "" or correo == "" or identificacion == "":
        messagebox.showerror(
            "Error",
            "Complete todos los datos del cliente"
        )
    else:
        messagebox.showinfo(
            "Registro",
            "Cliente registrado correctamente"
        )

# confirmar reserva 
def confirmar_reserva():

    nombre = entry_nombre.get()
    servicio = combo_servicio.get()
    horas = entry_horas.get()
    fecha = entry_fecha.get()

    # Costos según servicio
    costos = {
        "Hospedaje": 100,
        "Spa": 50,
        "Transporte": 30,
        "Tour": 80
    }

    if nombre == "" or servicio == "" or horas == "" or fecha == "":
        messagebox.showerror(
            "Error",
            "Complete todos los campos de reserva"
        )
        return

    costo = costos.get(servicio, 0)

    tabla.insert(
        "",
        "end",
        values=(
            nombre,
            servicio,
            horas,
            fecha,
            "Confirmada",
            f"${costo}"
        )
    )

    messagebox.showinfo(
        "Reserva",
        "Reserva confirmada correctamente"
    )

    limpiar_campos()


#cancelar reserva
def cancelar_reserva():

    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning(
            "Cancelar",
            "Seleccione una reserva"
        )
        return

    tabla.delete(seleccion)

    messagebox.showinfo(
        "Reserva",
        "Reserva cancelada"
    )


def limpiar_campos():

    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_identificacion.delete(0, tk.END)
    entry_horas.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)

    combo_servicio.set("")


# VENTANA PRINCIPAL
# =========================

ventana = tk.Tk()

ventana.title("Sistema de Reservas")
ventana.geometry("1000x700")
ventana.config(bg="#dce8f2")


# =========================
# TITULO
# =========================

titulo = tk.Label(
    ventana,
    text="Sistema de Reservas",
    font=("Arial", 24, "bold"),
    bg="#dce8f2",
    fg="#003366"
)

titulo.pack(pady=20)


# =========================
# FRAME PRINCIPAL
# =========================

frame = tk.Frame(
    ventana,
    bg="#dce8f2"
)

frame.pack()


# =========================
# DATOS CLIENTE
# =========================

label_nombre = tk.Label(
    frame,
    text="Ingrese nombre y apellido:",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_nombre.grid(
    row=0,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_nombre = tk.Entry(frame, width=30)

entry_nombre.grid(
    row=1,
    column=0,
    padx=20
)

# Ingreso de correo 
label_correo = tk.Label(
    frame,
    text="Ingrese el correo:",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_correo.grid(
    row=2,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_correo = tk.Entry(frame, width=30)

entry_correo.grid(
    row=3,
    column=0,
    padx=20
)

# Ingreso de identificacion 
label_identificacion = tk.Label(
    frame,
    text="Ingrese identificación:",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_identificacion.grid(
    row=4,
    column=0,
    padx=20,
    pady=10,
    sticky="w"
)

entry_identificacion = tk.Entry(frame, width=30)

entry_identificacion.grid(
    row=5,
    column=0,
    padx=20
)


# =========================
# DATOS RESERVA
# =========================

label_servicio = tk.Label(
    frame,
    text="Seleccione servicio:",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_servicio.grid(
    row=0,
    column=1,
    padx=60,
    pady=10,
    sticky="w"
)

combo_servicio = ttk.Combobox(
    frame,
    width=27,
    state="readonly"
)

# ============================================
# LISTA DE SERVICIOS
# ============================================

servicios = [

    "Hospedaje",
    "Spa",
    "Transporte",
    "Tour"

]

combo_servicio.grid(
    row=1,
    column=1,
    padx=60
)

# Ingreso de hora
label_horas = tk.Label(
    frame,
    text="Ingrese horas:",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_horas.grid(
    row=2,
    column=1,
    padx=60,
    pady=10,
    sticky="w"
)

entry_horas = tk.Entry(frame, width=30)

entry_horas.grid(
    row=3,
    column=1,
    padx=60
)

# Ingreso de fecha 
label_fecha = tk.Label(
    frame,
    text="Ingrese fecha: Dia/Mes/Año",
    bg="#dce8f2",
    font=("Arial", 10, "bold")
)

label_fecha.grid(
    row=4,
    column=1,
    padx=60,
    pady=10,
    sticky="w"
)

entry_fecha = tk.Entry(frame, width=30)

entry_fecha.grid(
    row=5,
    column=1,
    padx=60
)


# BOTONES
# =========================
# Boton registrar reserva 
btn_registrar = tk.Button(
    ventana,
    text="Registrar Cliente",
    bg="#007acc",
    fg="white",
    width=20,
    command=registrar_cliente
)

btn_registrar.place(x=100, y=330)

# Boton confirmar reserva 
btn_confirmar = tk.Button(
    ventana,
    text="Confirmar Reserva",
    bg="#2eb82e",
    fg="white",
    width=20,
    command=confirmar_reserva
)

btn_confirmar.place(x=430, y=330)

#Boton cancelar reserva
btn_cancelar = tk.Button(
    ventana,
    text="Cancelar Reserva",
    bg="#e60000",
    fg="white",
    width=20,
    command=cancelar_reserva
)

btn_cancelar.place(x=740, y=330)


# =========================
# TABLA
# =========================

columnas = (
    "Cliente",
    "Servicio",
    "Horas",
    "Fecha",
    "Estado",
    "Costo"
)

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=12
)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150, anchor="center")

tabla.place(x=50, y=400)


# =========================
# EJECUTAR
# =========================

ventana.mainloop()