# Modulo: reserva.py
# Define la entidad Reserva
#
# Conceptos aplicados:
# - Encapsulación
# - Asociación (Cliente + Servicio)
# - Manejo de excepciones

from cliente import Cliente
from servicio import Servicio, ServicioError


# Excepción personalizada para errores relacionados con reservas
class ReservaError(Exception):
    pass


class Reserva:

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: int):

        # Validación: el cliente debe ser una instancia de Cliente
        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        # Validación: el servicio debe ser una instancia de Servicio
        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        # Validación: la duración debe ser mayor a 0
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")

        # Atributos privados (encapsulación)
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "pendiente"  # Estado inicial de la reserva

    # =========================
    # MÉTODOS DE NEGOCIO
    # =========================

    def confirmar(self):
        # Solo se puede confirmar si está en estado pendiente
        if self.__estado != "pendiente":
            raise ReservaError("La reserva no se puede confirmar")

        # Cambio de estado
        self.__estado = "confirmada"

        # Registro en logs
        self._log("Reserva confirmada")

    def cancelar(self):
        # No se puede cancelar si ya está cancelada
        if self.__estado == "cancelada":
            raise ReservaError("La reserva ya está cancelada")

        # Cambio de estado
        self.__estado = "cancelada"

        # Registro en logs
        self._log("Reserva cancelada")

    def procesar(self):
        """
        Calcula el costo usando polimorfismo del servicio
        """
        try:
            # Se calcula el costo usando el método del servicio
            costo = self.__servicio.calcular_costo(horas=self.__duracion)

            # Registro en logs
            self._log(f"Costo calculado: {costo}")

            return costo

        except Exception as e:
            # En caso de error, se registra en logs
            self._log(f"Error procesando reserva: {str(e)}")
            return None

    # =========================
    # LOGS
    # =========================

    def _log(self, mensaje):
        # Método privado para registrar eventos en archivo logs.txt
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