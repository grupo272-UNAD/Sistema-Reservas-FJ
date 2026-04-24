"""
Interfaz de prueba para el módulo de servicios.

Permite:
✔ Seleccionar servicio
✔ Ingresar horas
✔ Calcular costo
"""

import tkinter as tk
from tkinter import ttk, messagebox

from modelos.servicios_derivados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

# -----------------------------
# SERVICIOS DISPONIBLES
# -----------------------------
servicios = {
    "Reserva Sala": ReservaSala("Sala", 50000),
    "Alquiler Equipo": AlquilerEquipo("Laptop", 30000),
    "Asesoría": AsesoriaEspecializada("Consultoría", 80000)
}

# -----------------------------
# FUNCIÓN CALCULAR
# -----------------------------
def calcular():
    try:
        if combo_servicio.get() == "":
            raise ValueError("Seleccione un servicio")

        if entry_horas.get() == "":
            raise ValueError("Ingrese las horas")

        servicio = servicios[combo_servicio.get()]
        horas = float(entry_horas.get())

        costo = servicio.calcular_costo(horas)

        resultado.config(text=f"Costo: ${costo:,.0f}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -----------------------------
# INTERFAZ
# -----------------------------
ventana = tk.Tk()
ventana.title("Módulo Servicios")
ventana.geometry("300x250")

tk.Label(ventana, text="Servicio").pack()
combo_servicio = ttk.Combobox(
    ventana,
    values=list(servicios.keys())
)
combo_servicio.pack()

tk.Label(ventana, text="Horas").pack()
entry_horas = tk.Entry(ventana)
entry_horas.pack()

tk.Button(
    ventana,
    text="Calcular costo",
    command=calcular
).pack(pady=10)

resultado = tk.Label(ventana, text="Costo: $0")
resultado.pack()

ventana.mainloop()
