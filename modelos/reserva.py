"""
Modulo: reserva.py
Define la entidad Reserva

Conceptos aplicados:
- Encapsulación
- Asociación (Cliente + Servicio)
- Manejo de excepciones
"""

from modelos.cliente import Cliente
from modelos.servicio import Servicio, ServicioError


class ReservaError(Exception):
    """Excepción personalizada para reservas"""
    pass


class Reserva:

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "pendiente"

    # =========================
    # MÉTODOS DE NEGOCIO
    # =========================

    def confirmar(self):
        if self.__estado != "pendiente":
            raise ReservaError("La reserva no se puede confirmar")

        self.__estado = "confirmada"
        self._log("Reserva confirmada")

    def cancelar(self):
        if self.__estado == "cancelada":
            raise ReservaError("La reserva ya está cancelada")

        self.__estado = "cancelada"
        self._log("Reserva cancelada")

    def procesar(self):
        """
        Calcula el costo usando polimorfismo del servicio
        """
        try:
            costo = self.__servicio.calcular_costo(horas=self.__duracion)
            self._log(f"Costo calculado: {costo}")
            return costo

        except Exception as e:
            self._log(f"Error procesando reserva: {str(e)}")
            return None

    # =========================
    # LOGS
    # =========================

    def _log(self, mensaje):
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(mensaje + "\n")
        except:
            print("Error en logs")

    # =========================
    # GETTERS
    # =========================

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado