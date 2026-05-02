"""
Modulo: gestor_reserva.py

Gestiona reservas del sistema

Conceptos:
- Manejo de listas
- Manejo de excepciones
- Logs
"""

from modelos.reserva import Reserva, ReservaError


class GestorReserva:

    def __init__(self):
        self._reservas = []

    # =========================
    # CRUD RESERVAS
    # =========================

    def registrar_reserva(self, reserva: Reserva):
        try:
            if reserva is None:
                raise ReservaError("La reserva no puede ser None")

            self._reservas.append(reserva)
            self._log("Reserva registrada correctamente")

        except ReservaError as e:
            self._log(f"Error al registrar reserva: {str(e)}")

    def listar_reservas(self):
        return self._reservas

    def buscar_reserva(self, id_cliente):
        """
        Busca reserva por ID de cliente
        """
        try:
            for reserva in self._reservas:
                if reserva.cliente.idCliente == id_cliente:
                    return reserva

            raise ReservaError("Reserva no encontrada")

        except ReservaError as e:
            self._log(str(e))
            return None

    def cancelar_reserva(self, id_cliente):
        try:
            reserva = self.buscar_reserva(id_cliente)

            if reserva is None:
                raise ReservaError("No existe reserva para cancelar")

            reserva.cancelar()
            self._log("Reserva cancelada correctamente")

        except ReservaError as e:
            self._log(f"Error al cancelar: {str(e)}")

    def confirmar_reserva(self, id_cliente):
        try:
            reserva = self.buscar_reserva(id_cliente)

            if reserva is None:
                raise ReservaError("No existe reserva para confirmar")

            reserva.confirmar()
            self._log("Reserva confirmada correctamente")

        except ReservaError as e:
            self._log(f"Error al confirmar: {str(e)}")

    def calcular_costo_reserva(self, id_cliente):
        try:
            reserva = self.buscar_reserva(id_cliente)

            if reserva is None:
                raise ReservaError("Reserva no encontrada")

            return reserva.procesar()

        except Exception as e:
            self._log(f"Error en cálculo: {str(e)}")
            return None

    # =========================
    # LOGS
    # =========================

    def _log(self, mensaje):
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(mensaje + "\n")
        except:
            print("Error escribiendo logs")