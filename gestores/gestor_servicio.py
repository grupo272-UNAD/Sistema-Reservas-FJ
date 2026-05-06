"""
Modulo: gestor_servicio.py
Gestiona los servicios del sistema.
- Manejo de listas
- Manejo de excepciones
- Registro de logs
"""

# 1. TODOS LOS IMPORTS 
from modelos.servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria,
    ServicioError
)
# 2. Nueva excepción de utilidades
from utilidades.excepciones import DatoNoValidoError

class GestorServicio:
    def __init__(self):
        self._servicios = []

    def registrar_servicio(self, servicio):
        try:
            if servicio is None:
                raise ServicioError("El servicio no puede ser None")

            # VALIDACIONES
            if not servicio.nombre or servicio.nombre.strip() == "":
                raise DatoNoValidoError("El nombre del servicio no puede estar vacío")

            if servicio.precio <= 0:
                raise DatoNoValidoError("El precio del servicio debe ser mayor a 0")

            # REGISTRO
            self._servicios.append(servicio)
            self._log(f"Servicio '{servicio.nombre}' registrado correctamente")

        except (ServicioError, DatoNoValidoError) as e:
            self._log(f"Error al registrar servicio: {str(e)}")
            raise e # Esto le avisa a la interfaz que algo falló