"""
Modulo: servicio.py
Contiene la clase abstracta Servicio y sus implementaciones concretas.
Se aplican conceptos de:
- Abstracción (clase abstracta)
- Herencia
- Polimorfismo
- Encapsulación
"""

from abc import ABC, abstractmethod


class ServicioError(Exception):
    """Excepción personalizada para errores en servicios"""
    pass


class Servicio(ABC):
    """
    Clase abstracta base para todos los servicios.
    """

    def __init__(self, nombre: str, costo_base: float):
        if not nombre:
            raise ServicioError("El nombre del servicio no puede estar vacío")

        if costo_base <= 0:
            raise ServicioError("El costo base debe ser mayor que cero")

        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, tiempo: int) -> float:
        """
        Método abstracto que cada servicio debe implementar.
        Permite polimorfismo.
        """
        pass

    @abstractmethod
    def descripcion(self) -> str:
        """Descripción del servicio"""
        pass

    def calcular_costo_con_impuesto(self, impuesto: float = 0.19):
        """
        Método "sobrecargado" (simulado en Python con parámetros opcionales)
        """
        return self._costo_base * (1 + impuesto)

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base


# =========================
# SERVICIOS CONCRETOS
# =========================

class ServicioSala(Servicio):
    """Servicio de reserva de salas"""

    def __init__(self, nombre: str, costo_base: float, capacidad: int):
        super().__init__(nombre, costo_base)

        if capacidad <= 0:
            raise ServicioError("La capacidad debe ser mayor a 0")

        self._capacidad = capacidad

    def calcular_costo(self, tiempo: int = 1) -> float:
        if tiempo <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        return self._costo_base * tiempo

    def descripcion(self) -> str:
        return f"Sala con capacidad para {self._capacidad} personas"


class ServicioEquipo(Servicio):
    """Servicio de alquiler de equipos"""

    def __init__(self, nombre: str, costo_base: float, tipo_equipo: str):
        super().__init__(nombre, costo_base)

        if not tipo_equipo:
            raise ServicioError("Debe especificar el tipo de equipo")

        self._tipo_equipo = tipo_equipo

    def calcular_costo(self, tiempo: int = 1) -> float:
        if tiempo <= 0:
            raise ServicioError("Los días deben ser mayores a 0")

        return self._costo_base * tiempo

    def descripcion(self) -> str:
        return f"Alquiler de equipo tipo: {self._tipo_equipo}"


class ServicioAsesoria(Servicio):
    """Servicio de asesoría especializada"""

    def __init__(self, nombre: str, costo_base: float, especialidad: str):
        super().__init__(nombre, costo_base)

        if not especialidad:
            raise ServicioError("Debe especificar la especialidad")

        self._especialidad = especialidad

    def calcular_costo(self, tiempo: int = 1, descuento: float = 0) -> float:
        if tiempo <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        if descuento < 0 or descuento > 1:
            raise ServicioError("El descuento debe estar entre 0 y 1")

        total = self._costo_base * tiempo
        return total * (1 - descuento)

    def descripcion(self) -> str:
        return f"Asesoría en: {self._especialidad}"
    
