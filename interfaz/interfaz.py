#Karen Marcela Chara Mina
# Fase 4 


#Importamos la biblioteca tkinter para crear la interface
#Importamos el módulo messagebox de tkinter para mostrar mensajes emergentes

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import re

# =========================================================
# 1. CLASES Y LÓGICA DE NEGOCIO (MODELOS)
# =========================================================

class Servicio:
    """Clase Base para demostrar Polimorfismo."""
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    def calcular_costo(self, horas):
        return self.precio_base * horas

class ServicioSala(Servicio):
    def calcular_costo(self, horas):
        # Polimorfismo: Costo base + cargo fijo de limpieza
        return (self.precio_base * horas) + 20

class ServicioEquipo(Servicio):
    def calcular_costo(self, horas):
        # Polimorfismo: Costo estándar
        return self.precio_base * horas

class ServicioAsesoria(Servicio):
    def calcular_costo(self, horas):
        # Polimorfismo: Descuento del 10% si supera las 3 horas
        total = self.precio_base * horas
        return total * 0.9 if horas > 3 else total

class Cliente:
    """Clase base para datos del cliente."""
    def __init__(self, nombre, correo, id_cliente):
        self.nombre = nombre
        self.correo = correo
        self.id_cliente = id_cliente

class ValidacionCliente(Cliente):
    """Aplica Herencia: extiende Cliente con métodos de validación."""
    def validar_todo(self):
        if not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if "@" not in self.correo or "." not in self.correo:
            raise ValueError("El correo electrónico no es válido.")
        if not self.id_cliente.strip() or not self.id_cliente.isdigit():
            raise ValueError("La identificación debe ser un número válido.")
        return True

# Lista global para registros en memoria
ListaRegistros = []

# =========================================================
# 2. LÓGICA DE FUNCIONES (CONTROLADORES)
# =========================================================

def registrar_cliente():
    """Valida y registra al cliente en la lista global."""
    nombre = entry_nombre.get().strip()
    correo = entry_correo.get().strip()
    ident = entry_identificacion.get().strip()

    try:
        nuevo_cliente = ValidacionCliente(nombre, correo, ident)
        # Corregido: Llamada al método correcto 'validar_todo'
        if nuevo_cliente.validar_todo():
            ListaRegistros.append(nuevo_cliente)
            messagebox.showinfo("Éxito", f"Cliente {nombre} registrado en el sistema.")
    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))

# Confirmar reserva
def confirmar_reserva():
    """Procesa la reserva, calcula el costo y la añade a la tabla."""
    nombre = entry_nombre.get().strip()
    servicio = combo_servicio.get()
    horas = entry_horas.get().strip()
    fecha = entry_fecha.get().strip()
    patron = r"^\d{2}/\d{2}/\d{4}$"
    
    if not re.match(patron, fecha):
        messagebox.showerror("Error de Fecha", "La fecha debe tener el formato DD/MM/AAAA")
        return # Esto detiene la función para que no se guarde nada

    if not (nombre and servicio and horas and fecha):
        messagebox.showerror("Error", "Faltan datos para procesar la reserva.")
        return

    try:
        horas_int = int(horas)
        
        # Polimorfismo: Selección de objeto según el servicio
        if servicio == "Sala":
            obj = ServicioSala("Sala VIP", 100) 
        elif servicio == "Equipo":
            obj = ServicioEquipo("Computador", 50)
        elif servicio == "Asesoria":
            obj = ServicioAsesoria("Asesoría POO", 80)

        costo_final = obj.calcular_costo(horas_int)

        # Inserción en la tabla (Simula el paso de datos a la base de datos)
        tabla.insert("", tk.END, values=(
            nombre, servicio, horas, fecha, "Confirmada", f"${costo_final:,}"
        ))

        # Registro en logs.txt (Persistencia)
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - Cliente: {nombre} - Costo: ${costo_final}\n")

        messagebox.showinfo("Confirmación", f"Reserva confirmada por un total de ${costo_final}")
        limpiar_campos()

    except ValueError:
        messagebox.showerror("Error", "La cantidad de horas debe ser un número.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo confirmar: {str(e)}")

#Cancelar reserva
def cancelar_reserva():
    seleccion = tabla.selection()
    if seleccion:
        item = tabla.item(seleccion)
        nombre_cliente = item['values'][0] # Obtiene el nombre de la fila seleccionada
        
        if messagebox.askyesno("Confirmar", f"¿Desea cancelar la reserva de {nombre_cliente}?"):
            # Guardar cancelación en el log
            with open("logs.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} - CANCELADA - Cliente: {nombre_cliente}\n")
            
            tabla.delete(seleccion)
            messagebox.showinfo("Éxito", "Reserva cancelada y registrada.")

def limpiar_campos():
    """Limpia los widgets de entrada."""
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_identificacion.delete(0, tk.END)
    entry_horas.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    combo_servicio.set("")

# =========================================================
# 3. INTERFAZ GRÁFICA 
# =========================================================

def iniciar_interfaz():
    global entry_nombre, entry_correo, entry_identificacion, combo_servicio, entry_horas, entry_fecha, tabla

    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Reservas - UNAD")
    ventana.geometry("1100x850")
    ventana.configure(bg="#F4F6F7")

    # Título
    tk.Label(ventana, text="SISTEMA DE RESERVAS", font=("Segoe UI", 28, "bold"),
             bg="#F4F6F7", fg="#1B4F72", pady=20).pack()

    # Formulario
    frame_card = tk.Frame(ventana, bg="white", padx=30, pady=20, highlightbackground="#D5DBDB", highlightthickness=1)
    frame_card.pack(padx=50, fill="x")

    f_lbl = ("Segoe UI Semibold", 10)
    f_ent = ("Segoe UI", 11)

    # Fila 1
    tk.Label(frame_card, text="Nombre Completo", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=0, sticky="w")
    entry_nombre = tk.Entry(frame_card, font=f_ent, highlightthickness=1, highlightbackground="#D5DBDB", relief="flat")
    entry_nombre.grid(row=1, column=0, sticky="ew", padx=(0,15), pady=5, ipady=4)

    tk.Label(frame_card, text="Correo Electrónico", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=1, sticky="w")
    entry_correo = tk.Entry(frame_card, font=f_ent, highlightthickness=1, highlightbackground="#D5DBDB", relief="flat")
    entry_correo.grid(row=1, column=1, sticky="ew", padx=10, pady=5, ipady=4)

    tk.Label(frame_card, text="Identificación", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=0, column=2, sticky="w")
    entry_identificacion = tk.Entry(frame_card, font=f_ent, highlightthickness=1, highlightbackground="#D5DBDB", relief="flat")
    entry_identificacion.grid(row=1, column=2, sticky="ew", padx=(15,0), pady=5, ipady=4)

    # Fila 2
    tk.Label(frame_card, text="Tipo de Servicio", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=0, sticky="w", pady=(15,0))
    combo_servicio = ttk.Combobox(frame_card, font=f_ent, state="readonly", values=["Sala", "Equipo", "Asesoria"])
    combo_servicio.grid(row=3, column=0, sticky="ew", padx=(0,15), pady=5)

    tk.Label(frame_card, text="Horas", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=1, sticky="w", pady=(15,0))
    entry_horas = tk.Entry(frame_card, font=f_ent, highlightthickness=1, highlightbackground="#D5DBDB", relief="flat")
    entry_horas.grid(row=3, column=1, sticky="ew", padx=10, pady=5, ipady=4)

    tk.Label(frame_card, text="Fecha (DD/MM/AAAA)", font=f_lbl, bg="white", fg="#5D6D7E").grid(row=2, column=2, sticky="w", pady=(15,0))
    entry_fecha = tk.Entry(frame_card, font=f_ent, highlightthickness=1, highlightbackground="#D5DBDB", relief="flat")
    entry_fecha.grid(row=3, column=2, sticky="ew", padx=(15,0), pady=5, ipady=4)

    for i in range(3): frame_card.columnconfigure(i, weight=1)

    # Botones
    frame_btns = tk.Frame(ventana, bg="#F4F6F7")
    frame_btns.pack(pady=30)

 
    btns = [
        ("Registrar Cliente", "#2E86C1", registrar_cliente),
        ("Confirmar Reserva", "#28B463", confirmar_reserva),
        ("Cancelar Reserva", "#CB4335", cancelar_reserva)
    ]

    for i, (txt, col, cmd) in enumerate(btns):
        tk.Button(frame_btns, text=txt, bg=col, fg="white", font=("Segoe UI", 10, "bold"),
                  width=20, height=2, relief="flat", cursor="hand2", command=cmd).grid(row=0, column=i, padx=15)

    # Tabla de Resultados
    frame_tabla = tk.Frame(ventana, bg="white")
    frame_tabla.pack(padx=50, fill="both", expand=True, pady=(0,20))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=("Segoe UI Semibold", 10), background="#E5E8E8")
    
    columnas = ("Cliente", "Servicio", "Horas", "Fecha", "Estado", "Costo")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col.upper())
        tabla.column(col, width=150, anchor="center")

    tabla.pack(side="left", fill="both", expand=True)
    
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()