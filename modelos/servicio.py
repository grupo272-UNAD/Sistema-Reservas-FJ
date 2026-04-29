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
    def calcular_costo(self, **kwargs) -> float:
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


