# Fase 4 - Sistema de Reservas Funcional

# Importacion de las bibliotecar tkinet y messagebox para la interfaz y mostrar mensajes.
# Importamos los modelos principales del proyecto
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import re
from modelos.cliente import Cliente
from modelos.servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from modelos.reserva import Reserva


class DatoNoValidoError(Exception):
    """Lanzada cuando la entrada del usuario no cumple los requisitos."""
    pass

# PERSISTENCIA Y REGISTRO DE EVENTOS (LOGS)

def escribir_log(mensaje, nivel="INFO"):
    """Registra eventos y errores en 'logs.txt'."""
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"[{ahora}] [{nivel}] {mensaje}\n")
    except Exception as e:
        print(f"Error crítico escribiendo log: {e}")


# CONTROLADORES (LOGICA Y SIMULACION)

def confirmar_reserva():
    """Captura datos de la UI y gestiona la creación de una reserva."""
    nom = entry_nombre.get().strip()
    correo = entry_correo.get().strip()
    ident = entry_identificacion.get().strip()
    serv_tipo = combo_servicio.get()
    horas_s = entry_horas.get().strip()
    fecha = entry_fecha.get().strip()

    try:
        # Validación de campos obligatorios
        if not all([nom, correo, ident, serv_tipo, horas_s, fecha]):
            raise DatoNoValidoError("Por favor, complete todos los campos.")
        
        # Validación de formato de fecha
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", fecha):
            raise DatoNoValidoError("Fecha inválida. Use el formato DD/MM/AAAA.")

        # Creación del Cliente 
        obj_cli = Cliente(nom, correo, ident)

        # Creación del Servicio 
        if serv_tipo == "Sala":
            obj_serv = ServicioSala("Sala A", 100, capacidad=10) # Ajusta argumentos según tu modelo
        elif serv_tipo == "Equipo":
            obj_serv = ServicioEquipo("Computador Pro", 50)
        else:
            obj_serv = ServicioAsesoria("Mentoría Técnica", 80)

        # Creación de la Reserva 
        nueva_reserva = Reserva(obj_cli, obj_serv, int(horas_s), fecha)
        
        # Procesar costo 
        costo_final = obj_serv.calcular_costo(int(horas_s))

        # Actualización visual y logs
        tabla.insert("", tk.END, values=(nom, serv_tipo, horas_s, fecha, "Confirmada", f"${costo_final:,.2f}"))
        escribir_log(f"RESERVA MANUAL EXITOSA: Cliente {nom} | Servicio {serv_tipo}")
        messagebox.showinfo("Éxito", "La reserva ha sido procesada correctamente.")
        limpiar_campos()

    #Excepcion
    except Exception as e:
        escribir_log(f"ERROR EN OPERACIÓN: {type(e).__name__} - {str(e)}", "ERROR")
        messagebox.showerror("Error de Procesamiento", str(e))

def ejecutar_simulacion():
    """Simula 10 operaciones para demostrar robustez y manejo de exepciones."""
    casos = [
        ("Juan Perez", "juan@mail.com", "12345", "Sala", "2", "10/05/2026", "VÁLIDO"),
        ("", "error@mail.com", "555", "Equipo", "1", "11/05/2026", "ERROR: Nombre vacío"),
        ("Marta Gomez", "marta@mail.com", "abcde", "Asesoria", "3", "12/05/2026", "ERROR: ID no numérica"),
        ("Carlos Ruiz", "carlos@mail.com", "67890", "Equipo", "5", "13-05-2026", "ERROR: Fecha mal formato"),
        ("Ana López", "ana@mail.com", "11223", "Sala", "4", "14/05/2026", "VÁLIDO"),
        ("Pedro Picapiedra", "pedro@mail", "44556", "Asesoria", "1", "15/05/2026", "ERROR: Correo sin punto"),
        ("Lucia Sanz", "lucia@mail.com", "99887", "Inexistente", "2", "16/05/2026", "ERROR: Servicio inválido"),
        ("Roberto Carlos", "roberto@mail.com", "33445", "Equipo", "2", "17/05/2026", "VÁLIDO"),
        ("Karen Marcela", "karen@unad.edu.co", "100200", "Asesoria", "5", "20/05/2026", "VÁLIDO"),
        ("Usuario Final", "final@mail.com", "999", "Sala", "letras", "21/05/2026", "ERROR: Horas no numéricas")
    ]

    escribir_log("--- INICIANDO SIMULACIÓN DE 10 OPERACIONES ---")
    exitos = 0
    fallos = 0
    
    for i, (n, c, ide, s_t, h, f, desc) in enumerate(casos, 1):
        try:
            # Validacion de campos obligatorios
            if not n: raise DatoNoValidoError("El nombre no puede estar vacío.")
            if "@" not in c or "." not in c: raise DatoNoValidoError("Correo electrónico con formato inválido.")
            if not ide.isdigit(): raise DatoNoValidoError("La identificación debe ser numérica.")
            if not h.isdigit(): raise DatoNoValidoError("Las horas deben ser numéricas.")
            if not re.match(r"^\d{2}/\d{2}/\d{4}$", f): raise DatoNoValidoError("Fecha inválida.")

            cli = Cliente(n, c, ide)
            
            if s_t == "Sala": serv = ServicioSala("Sala Sim", 100, 5) # Ajusta parámetros
            elif s_t == "Equipo": serv = ServicioEquipo("PC Sim", 50, 'Computador de mesa')
            elif s_t == "Asesoria": serv = ServicioAsesoria("Asesoria Sim", 80, 'Sistemas')
            else: raise DatoNoValidoError("Servicio no reconocido")

            res = Reserva(cli, serv, int(h))
            costo = serv.calcular_costo(int(h))
            
            # Insertar registro exitoso
            tabla.insert("", tk.END, values=(n, s_t, h, f, "Confirmada", f"${costo:,.2f}"))
            escribir_log(f"Simulación #{i}: ÉXITO - {desc}")
            exitos += 1

        except Exception as e:
            # Insertar registro fallido con Tag de color rojo para demostrar manejo de error
            error_msg = f"FALLIDO: {str(e)}"
            tabla.insert("", tk.END, values=(n if n else "N/A", s_t, h, f, error_msg, "$0.00"), tags=('error_row',))
            escribir_log(f"Simulación #{i}: FALLO CONTROLADO - {desc} | Motivo: {str(e)}", "WARNING")
            fallos += 1

    messagebox.showinfo("Simulación Completa", f"Se ejecutaron 10 pruebas:\n- Exitosas: {exitos}\n- Fallidas: {fallos}\n\nRevisa la tabla y logs.txt.")
 
 #Limpiar
def limpiar_campos():
    for e in [entry_nombre, entry_correo, entry_identificacion, entry_horas, entry_fecha]:
        e.delete(0, tk.END)
    combo_servicio.set("")

# Función auxiliar para validar que solo entren números
def solo_numeros(char):
    return char.isdigit() or char == ""

# =========================================================
# 4. VISTA (INTERFAZ GRÁFICA TKINTER) - INTACTA
# =========================================================
def iniciar_interfaz():
    global entry_nombre, entry_correo, entry_identificacion, combo_servicio, entry_horas, entry_fecha, tabla

    ventana = tk.Tk()
    ventana.title("Sistema de Reservas FJ - Fase 4")
    ventana.geometry("1150x850")
    ventana.configure(bg="#F4F6F7")
    
    # Registro de validación numérica
    vcmd = (ventana.register(solo_numeros), '%S')

    # Título Principal
    tk.Label(ventana, text="SISTEMA DE GESTIÓN DE RESERVAS", font=("Segoe UI", 24, "bold"), bg="#F4F6F7", fg="#1B4F72", pady=25).pack()

    # Formulario
    frame_card = tk.Frame(ventana, bg="white", padx=30, pady=25, highlightbackground="#D5DBDB", highlightthickness=1)
    frame_card.pack(padx=40, fill="x")

    lbl_s = {"font": ("Segoe UI Semibold", 10), "bg": "white", "fg": "#5D6D7E"}
    ent_s = {"font": ("Segoe UI", 11), "highlightthickness": 1, "highlightbackground": "#D5DBDB", "relief": "flat"}
    
    # Fila 1
    #Nombre del cliente
    tk.Label(frame_card, text="Nombre del Cliente", **lbl_s).grid(row=0, column=0, sticky="w")
    entry_nombre = tk.Entry(frame_card, **ent_s); entry_nombre.grid(row=1, column=0, sticky="ew", padx=10, pady=5, ipady=4)
    
    #Correo electronico
    tk.Label(frame_card, text="Correo Electrónico", **lbl_s).grid(row=0, column=1, sticky="w")
    entry_correo = tk.Entry(frame_card, **ent_s); entry_correo.grid(row=1, column=1, sticky="ew", padx=10, pady=5, ipady=4)
    
    #ID
    tk.Label(frame_card, text="Identificación (ID)", **lbl_s).grid(row=0, column=2, sticky="w")
    # Se agrega validación de solo números
    entry_identificacion = tk.Entry(frame_card, **ent_s, validate='key', validatecommand=vcmd)
    entry_identificacion.grid(row=1, column=2, sticky="ew", padx=10, pady=5, ipady=4)
    
    # Fila 2
    #Tipo de servicio
    tk.Label(frame_card, text="Tipo de Servicio", **lbl_s).grid(row=2, column=0, sticky="w", pady=(15,0))
    combo_servicio = ttk.Combobox(frame_card, font=("Segoe UI", 11), state="readonly", values=["Sala", "Equipo", "Asesoria"])
    combo_servicio.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    
    # Tiempo de duracion (horas)
    tk.Label(frame_card, text="Duración (Horas)", **lbl_s).grid(row=2, column=1, sticky="w", pady=(15,0))
    # Se agrega validación de solo números
    entry_horas = tk.Entry(frame_card, **ent_s, validate='key', validatecommand=vcmd)
    entry_horas.grid(row=3, column=1, sticky="ew", padx=10, pady=5, ipady=4)
    
    #Fecha 
    tk.Label(frame_card, text="Fecha (DD/MM/AAAA)", **lbl_s).grid(row=2, column=2, sticky="w", pady=(15,0))
    entry_fecha = tk.Entry(frame_card, **ent_s); entry_fecha.grid(row=3, column=2, sticky="ew", padx=10, pady=5, ipady=4)

    for i in range(3): frame_card.columnconfigure(i, weight=1)

    # Panel de Control
    frame_btns = tk.Frame(ventana, bg="#F4F6F7")
    frame_btns.pack(pady=30)
    
    # Botones
    tk.Button(frame_btns, text="Procesar Reserva", bg="#28B463", fg="white", font=("Segoe UI", 10, "bold"), 
              width=22, height=2, command=confirmar_reserva, cursor="hand2", relief="flat").pack(side="left", padx=15)
    
    tk.Button(frame_btns, text="Simulación (Operaciones)", bg="#F39C12", fg="white", font=("Segoe UI", 10, "bold"), 
              width=25, height=2, command=ejecutar_simulacion, cursor="hand2", relief="flat").pack(side="left", padx=15)

    # Tabla de Datos
    frame_tabla = tk.Frame(ventana, bg="white")
    frame_tabla.pack(padx=40, fill="both", expand=True, pady=(0,20))
    
    #Columnas
    columnas = ("Cliente", "Servicio", "Horas", "Fecha", "Estado", "Costo Final")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    # Configuración de tags para colores
    tabla.tag_configure('error_row', foreground='#C0392B') 

    for col in columnas:
        tabla.heading(col, text=col.upper())
        tabla.column(col, width=150, anchor="center")
    
    tabla.pack(side="left", fill="both", expand=True)
    scrolly = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrolly.set); scrolly.pack(side="right", fill="y")

    escribir_log("Aplicación iniciada por el usuario.")
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()