import tkinter as tk #Importamos la biblioteca tkinter para crear la interface.
from tkinter import messagebox # Importamos el módulo messagebox de tkinter para mostrar mensajes emergentes.
from tkinter import ttk # Importamos el módulo ttk de tkinter para usar widgets más avanzados como Treeview.
from modelos.cliente import Cliente # Importamos la clase Cliente desde el módulo cliente.


class ValidacionCliente(Cliente): # Creamos la clase ValidacionCliente para validar los datos ingresados por el usuario.

    def validarNombre(self, nombre): # Creamos el metodo validarNombre para validar el nombre ingresado por el usuario.
        
        if nombre == "": # Validamos que el campo no esté vacío.
            raise ValueError("Datos ingresados incompletos") # Si el campo está vacío, lanzamos una excepción con un mensaje de error.
        
        if not nombre.replace(" ", "").isalpha(): # Validamos que el nombre no contenga números, ademas de permitir espacios en blanco.
            raise ValueError("El nombre no puede contener números") # Si el nombre contiene números, lanzamos una excepción con un mensaje de error.
        
        if not nombre.strip(): # Validamos que el nombre no contenga solo espacios en blanco.
            raise ValueError("El campo no puede estar vacío ni contener solo espacios en blanco.")
        
        if len(nombre) < 3: #Asi validamos que los datos no sean inferiores a 3 caracteres.
            raise ValueError("El nombre debe tener al menos 3 caracteres") # Si el nombre es demasiado corto, lanzamos una excepción con un mensaje de error.
        
        if len(set(nombre.lower().replace(" ", ""))) <= 1:# Validamos que el nombre no contenga solo un caracter repetido, ademas de permitir espacios en blanco.
            raise ValueError("El nombre no es válido.")
        
        else:
            return True # Retornamos true si el campo no está vacío.
    
    def ValidarCorreo(self, correo): # Creamos el metodo validarCorreo para validar el correo ingresado por el usuario.
        
        if correo == "": # Validamos que el campo no esté vacío.
            raise ValueError("Datos ingresados incompletos") # Si el campo está vacío, lanzamos una excepción con un mensaje de error.
        
        if "@" not in correo or "." not in correo: # Validamos que el correo contenga un @ y un punto.
            raise ValueError("Correo electrónico no válido") # Si el correo no contiene un @ o un punto, lanzamos una excepción con un mensaje de error.
        
        if correo.startswith("@") or correo.endswith("@") or correo.startswith(".") or correo.endswith("."): # Validamos que el correo no comience ni termine con un @ o un punto.
            raise ValueError("Correo electrónico no válido") # Si el correo comienza o termina con un @ o un punto, lanzamos una excepción con un mensaje de error.
        
        if len(correo) < 5: # Validamos que el correo tenga al menos 5 caracteres.
            raise ValueError("Correo electrónico no válido") # Si el correo es demasiado corto, lanzamos una excepción con un mensaje de error.
        
        if len(set(correo)) <= 2: # Validamos que el correo no contenga solo un caracter repetido.
            raise ValueError("El correo electrónico no es válido.")
        
        else:
            return True # Retornamos true si el campo no está vacío.  

    def validarIdCliente(self, idCliente): # Creamos el metodo validarIdCliente para validar el idCliente ingresado por el usuario.
        
        if idCliente == "": # Validamos que el campo no esté vacío.
            raise ValueError("Datos ingresados incompletos") # Si el campo está vacío, lanzamos una excepción con un mensaje de error.
        
        if not idCliente.isdigit(): # Validamos que el idCliente no contenga letras.
            raise ValueError("La identificación del cliente no puede contener letras") # Si el idCliente contiene letras, lanzamos una excepción con un mensaje de error.
        
        if len(idCliente) <6: # Validamos que el idCliente tenga al menos 6 caracteres.
            raise ValueError("Identificación inválida") #La cedula tiene 10 digitos, por lo que si el idCliente no tiene 10 caracteres, lanzamos una excepción con un mensaje de error.
        
        if len(set(idCliente)) <= 1:
            raise ValueError("La identificación no es válida.")
        
        else:
            return True # Retornamos true si el campo no está vacío.