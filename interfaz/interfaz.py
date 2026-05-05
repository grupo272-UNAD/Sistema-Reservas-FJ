#Karen Marcela Chara Mina
# Fase 4 


#Importamos la biblioteca tkinter para crear la interface
#Importamos el módulo messagebox de tkinter para mostrar mensajes emergentes

import tkinter as tk
from tkinter import ttk, messagebox
import re

# =========================================================
# 1. IMPORTAR CLASES (Capa de Negocio)
# =========================================================
try:
    # Se importan las clases del archivo externo modelos/servicio.py
    from modelos.servicio import (
        ServicioSala,
        ServicioEquipo,
        ServicioAsesoria,
        ServicioError
    )
except ImportError:
    # Definición de respaldo en caso de que el archivo no esté accesible
    class ServicioError(Exception): pass

# =========================================================
# 2. LÓGICA DE FUNCIONES
# =========================================================

def registrar_cliente():
    """Valida y registra la información del cliente."""
    nombre = entry_nombre.get().strip()
    correo = entry_correo.get().strip()
    id_cliente = entry_identificacion.get().strip()

    if not (nombre and correo and id_cliente):
        messagebox.showerror("Error", "Complete todos los campos del cliente.")
        return

    # Validación de formato de correo mediante expresiones regulares
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
        messagebox.showerror("Error", "Correo electrónico inválido.")
        return

    messagebox.showinfo("Registro", f"Cliente {nombre} registrado correctamente.")

def confirmar_reserva():
    # 1. Capturar datos de los Entry
    nombre = entry_nombre.get().strip()
    servicio = combo_servicio.get()
    horas = entry_horas.get().strip()
    fecha = entry_fecha.get().strip()

    # 2. Validación básica
    if not (nombre and servicio and horas and fecha):
        messagebox.showerror("Error", "Faltan datos para procesar la reserva.")
        return

    try:
        horas_int = int(horas)
        
        # 3. Crear el objeto según el servicio (Corrigiendo el error de argumentos)
        if servicio == "Sala":
            # Usamos 2 argumentos para coincidir con tu clase ServicioSala
            obj = ServicioSala("Sala VIP", 100) 
        elif servicio == "Equipo":
            obj = ServicioEquipo("Computador", 50)
        elif servicio == "Asesoria":
            obj = ServicioAsesoria("Asesoría POO", 80)

        # 4. Calcular el costo
        costo_final = obj.calcular_costo(horas_int)

        # 5. LA PARTE CLAVE: Insertar en la tabla "de abajo"
        # El orden de 'values' debe coincidir exactamente con tus columnas
        tabla.insert("", tk.END, values=(
            nombre,      # Columna 1: Cliente
            servicio,    # Columna 2: Servicio
            horas,       # Columna 3: Horas
            fecha,       # Columna 4: Fecha
            "Confirmada",# Columna 5: Estado
            f"${costo_final}" # Columna 6: Costo
        ))

        messagebox.showinfo("Éxito", "Reserva añadida a la lista correctamente.")
        limpiar_campos()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo confirmar: {str(e)}")

def cancelar_reserva():
    """Elimina la reserva seleccionada de la tabla."""
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione una reserva de la lista para cancelar.")
        return
    
    if messagebox.askyesno("Confirmar", "¿Desea cancelar la reserva seleccionada?"):
        tabla.delete(seleccion)
        messagebox.showinfo("Cancelado", "Reserva eliminada correctamente.")

def limpiar_campos():
    """Limpia los widgets de entrada de texto."""
    for widget in [entry_nombre, entry_correo, entry_identificacion, entry_horas, entry_fecha]:
        widget.delete(0, tk.END)
    combo_servicio.set("")

# =========================================================
# 3. INTERFAZ GRÁFICA (Capa de Presentación)
# =========================================================

def iniciar_interfaz():
    global entry_nombre, entry_correo, entry_identificacion, combo_servicio, entry_horas, entry_fecha, tabla

    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Reservas - UNAD")
    ventana.geometry("1100x800")
    ventana.configure(bg="#F4F6F7") # Fondo gris azulado claro
    ventana.resizable(False, False)

    # --- TÍTULO PRINCIPAL ---
    tk.Label(
        ventana, text="SISTEMA DE RESERVAS", font=("Segoe UI", 28, "bold"),
        bg="#F4F6F7", fg="#1B4F72", pady=20
    ).pack()

    # --- CONTENEDOR DEL FORMULARIO (ESTILO CARD) ---
    # Este marco agrupa las entradas en dos columnas centradas.
    frame_card = tk.Frame(ventana, bg="white", padx=30, pady=20, highlightbackground="#D5DBDB", highlightthickness=1)
    frame_card.pack(padx=50, fill="x")

    # Configuración de columnas del grid
    for i in range(3): frame_card.columnconfigure(i, weight=1)

    # Estilos de fuente
    f_lbl = ("Segoe UI Semibold", 10)
    f_ent = ("Segoe UI", 11)

    # Campos: Fila 1
    tk.Label(frame_card, text="Nombre Completo", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=0, sticky="w", pady=(10,0))
    entry_nombre = tk.Entry(frame_card, font=f_ent, relief="flat", highlightthickness=1, highlightbackground="#D5DBDB")
    entry_nombre.grid(row=1, column=0, sticky="ew", padx=(0,15), pady=5, ipady=4)

    tk.Label(frame_card, text="Correo Electrónico", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=1, sticky="w", pady=(10,0))
    entry_correo = tk.Entry(frame_card, font=f_ent, relief="flat", highlightthickness=1, highlightbackground="#D5DBDB")
    entry_correo.grid(row=1, column=1, sticky="ew", padx=10, pady=5, ipady=4)

    tk.Label(frame_card, text="Identificación", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=2, sticky="w", pady=(10,0))
    entry_identificacion = tk.Entry(frame_card, font=f_ent, relief="flat", highlightthickness=1, highlightbackground="#D5DBDB")
    entry_identificacion.grid(row=1, column=2, sticky="ew", padx=(15,0), pady=5, ipady=4)

    # Campos: Fila 2
    tk.Label(frame_card, text="Tipo de Servicio", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=0, sticky="w", pady=(15,0))
    combo_servicio = ttk.Combobox(frame_card, font=f_ent, state="readonly", values=["Sala", "Equipo", "Asesoria"])
    combo_servicio.grid(row=3, column=0, sticky="ew", padx=(0,15), pady=5)

    tk.Label(frame_card, text="Cantidad de Horas", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=1, sticky="w", pady=(15,0))
    entry_horas = tk.Entry(frame_card, font=f_ent, relief="flat", highlightthickness=1, highlightbackground="#D5DBDB")
    entry_horas.grid(row=3, column=1, sticky="ew", padx=10, pady=5, ipady=4)

    tk.Label(frame_card, text="Fecha (DD/MM/AAAA)", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=2, sticky="w", pady=(15,0))
    entry_fecha = tk.Entry(frame_card, font=f_ent, relief="flat", highlightthickness=1, highlightbackground="#D5DBDB")
    entry_fecha.grid(row=3, column=2, sticky="ew", padx=(15,0), pady=5, ipady=4)

    # --- SECCIÓN DE BOTONES ---
    frame_btns = tk.Frame(ventana, bg="#F4F6F7")
    frame_btns.pack(pady=30)

    def crear_btn(text, color, cmd, col):
        btn = tk.Button(frame_btns, text=text, bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                        width=20, height=2, relief="flat", cursor="hand2", command=cmd)
        btn.grid(row=0, column=col, padx=15)

    crear_btn("Registrar Cliente", "#2E86C1", registrar_cliente, 0)
    crear_btn("Confirmar Reserva", "#28B463", confirmar_reserva, 1)
    crear_btn("Cancelar Reserva", "#CB4335", cancelar_reserva, 2)

    # --- TABLA DE RESERVAS (RESULTADOS) ---
    frame_tabla = tk.Frame(ventana, bg="white")
    frame_tabla.pack(padx=50, fill="both", expand=True, pady=(0,20))

    # Estilo de la tabla
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=("Segoe UI Semibold", 10), background="#E5E8E8")
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=30)

    columnas = ("Cliente", "Servicio", "Horas", "Fecha", "Estado", "Costo")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col.upper())
        tabla.column(col, width=150, anchor="center")

    tabla.pack(side="left", fill="both", expand=True)
    
    # Scrollbar para la tabla
    scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scroll.set)
    scroll.pack(side="right", fill="y")

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()