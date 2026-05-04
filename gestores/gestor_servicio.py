"""
Modulo: gestor_servicio.py
Gestiona los servicios del sistema.

Conceptos aplicados:
- Manejo de listas: almacenamiento de servicios
- Manejo de excepciones: control de errores con ServicioError
- Registro de logs: seguimiento de acciones en archivo logs.txt
"""

from modelos.servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria,
    ServicioError
)


class GestorServicio:
    """
    Clase encargada de administrar los servicios del sistema.
    Permite registrar, buscar, eliminar y calcular costos.
    """

    def __init__(self):
        # Lista donde se almacenan todos los servicios registrados
        self._servicios = []

    def registrar_servicio(self, servicio):
        """
        Registra un servicio en el sistema.
        """
        try:
            # Validación: el servicio no puede ser nulo
            if servicio is None:
                raise ServicioError("El servicio no puede ser None")

            # Se agrega el servicio a la lista
            self._servicios.append(servicio)

            # Registro en logs
            self._log("Servicio registrado correctamente")

        except ServicioError as e:
            # Captura y registro del error
            self._log(f"Error al registrar servicio: {str(e)}")

    def listar_servicios(self):
        """
        Devuelve la lista de todos los servicios registrados.
        """
        return self._servicios

    def buscar_servicio(self, nombre):
        """
        Busca un servicio por su nombre.
        """
        try:
            # Recorre la lista de servicios
            for servicio in self._servicios:
                if servicio.nombre == nombre:
                    return servicio

            # Si no se encuentra, lanza excepción
            raise ServicioError("Servicio no encontrado")

        except ServicioError as e:
            self._log(str(e))
            return None

    def eliminar_servicio(self, nombre):
        """
        Elimina un servicio del sistema.
        """
        try:
            # Busca el servicio antes de eliminar
            servicio = self.buscar_servicio(nombre)

            if servicio is None:
                raise ServicioError("No se puede eliminar un servicio inexistente")

            # Elimina el servicio de la lista
            self._servicios.remove(servicio)

            # Registro en logs
            self._log("Servicio eliminado correctamente")

        except ServicioError as e:
            self._log(f"Error al eliminar servicio: {str(e)}")

    def calcular_costo_servicio(self, nombre, **kwargs):
        """
        Calcula el costo de un servicio usando polimorfismo.
        """
        try:
            # Busca el servicio
            servicio = self.buscar_servicio(nombre)

            if servicio is None:
                raise ServicioError("Servicio no encontrado para cálculo")

            # Llama al método polimórfico del servicio
            return servicio.calcular_costo(**kwargs)

        except Exception as e:
            # Captura cualquier error y lo registra
            self._log(f"Error en cálculo de costo: {str(e)}")
            return None

    def _log(self, mensaje):
        """
        Registra eventos del sistema en el archivo logs.txt.
        Permite llevar un historial de acciones y errores.
        """
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(mensaje + "\n")
        except Exception as e:
            print("Error escribiendo en logs:", e)