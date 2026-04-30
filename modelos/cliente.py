import tkinter as tk #Importamos la biblioteca tkinter para crear la interface.
from tkinter import messagebox # Importamos el módulo messagebox de tkinter para mostrar mensajes emergentes.


class Cliente: # Creamos la clase cliente.

    def __init__(self, nombre, correo, idCliente): # Creamos el metodo constructor de la clase cliente.
        
        self.__nombre=nombre 
        self.__correo=correo
        self.__idCliente=idCliente

    @property # Creamos el metodo getter para el atributo nombre.
    def nombre(self): #
        return self.__nombre # Retornamos el valor del atributo nombre.

    @property 
    def correo(self):
        return self.__correo
    
    @property
    def idCliente(self):
        return self.__idCliente