# Modulo: reserva.py
# Define la entidad Reserva
#
# Conceptos aplicados:
# - Encapsulación
# - Asociación (Cliente + Servicio)
# - Manejo de excepciones

from cliente import Cliente
from servicio import Servicio


# Excepción personalizada para errores relacionados con reservas
class ReservaError(Exception):
    pass

   
class Reserva:

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):

        # Validación: el cliente debe ser una instancia de Cliente
        if not cliente:
            raise ReservaError("Cliente inválido")
            
           
        # Validación: el servicio debe ser una instancia de Servicio
        if not servicio:
            raise ReservaError("Servicio inválido")

        # Validación: la duración debe ser mayor a 0
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        # Atributos privados (encapsulación)
        self.__cliente = cliente
        self.__servicio = Servicio
        self.__duracion = duracion
        self.__estado = "pendiente"  # Estado inicial de la reserva

    # =========================
    # GETTERS
    # =========================

    @property
    def cliente(self):
        # Retorna el cliente asociado a la reserva
        return self.__cliente

    @property
    def servicio(self):
        # Retorna el servicio asociado
        return self.__servicio

    @property
    def duracion(self):
        # Retorna la duración de la reserva
        return self.__duracion

    @property
    def estado(self):
        # Retorna el estado actual de la reserva
        return self.__estado