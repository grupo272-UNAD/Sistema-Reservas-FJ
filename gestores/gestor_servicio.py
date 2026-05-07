"""
Modulo: gestor_servicio.py
Gestiona los servicios del sistema.
- Manejo de listas
- Manejo de excepciones
- Registro de logs
"""

from modelos.servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria,
    ServicioError
)


class GestorServicio:
    """
    Clase encargada de administrar los servicios
    """

    def __init__(self):
        self._servicios = []

    def registrar_servicio(self, servicio):
        """
        Registra un servicio en el sistema
        """
        try:
            if servicio is None:
                raise ServicioError("El servicio no puede ser None")

            self._servicios.append(servicio)
            self._log(f"Servicio registrado correctamente: {servicio.nombre} | Tipo: {type(servicio).__name__})")

        except ServicioError as e:
            self._log(f"Error al registrar servicio: {str(e)}")

    def listar_servicios(self):
        """Devuelve todos los servicios"""
        return self._servicios

    def buscar_servicio(self, nombre):
        """
        Busca un servicio por nombre
        """
        try:
            for servicio in self._servicios:
                if servicio.nombre == nombre:
                    return servicio

            raise ServicioError("Servicio no encontrado")

        except ServicioError as e:
            self._log(str(e))
            return None

    def eliminar_servicio(self, nombre):
        """
        Elimina un servicio del sistema
        """
        try:
            servicio = self.buscar_servicio(nombre)

            if servicio is None:
                raise ServicioError("No se puede eliminar un servicio inexistente")

            self._servicios.remove(servicio)
            self._log("Servicio eliminado correctamente")

        except ServicioError as e:
            self._log(f"Error al eliminar servicio: {str(e)}")

    def calcular_costo_servicio(self, nombre, **kwargs):
        """
        Calcula el costo de un servicio usando polimorfismo
        """
        try:
            servicio = self.buscar_servicio(nombre)

            if servicio is None:
                raise ServicioError("Servicio no encontrado para cálculo")

            return servicio.calcular_costo(**kwargs)

        except Exception as e:
            self._log(f"Error en cálculo de costo: {str(e)}")
            return None

    def _log(self, mensaje):
        """
        Registra eventos en archivo logs.txt
        """
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(mensaje + "\n")
        except Exception as e:
            print("Error escribiendo en logs:", e)




