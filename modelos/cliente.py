def registrar_cliente_interfaz():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    id_cli = entry_identificacion.get()

    exito, mensaje = registrarCliente(nombre, correo, id_cli)
    
    if exito:
        messagebox.showinfo("Registro exitoso", mensaje)
    else:
        messagebox.showerror("Error de Validación", mensaje)
        