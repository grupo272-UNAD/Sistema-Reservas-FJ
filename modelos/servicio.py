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

    def calcular_costo(self, horas: int = 1) -> float:
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        return self._costo_base * horas

    def descripcion(self) -> str:
        return f"Sala con capacidad para {self._capacidad} personas"


class ServicioEquipo(Servicio):
    """Servicio de alquiler de equipos"""

    def __init__(self, nombre: str, costo_base: float, tipo_equipo: str):
        super().__init__(nombre, costo_base)

        if not tipo_equipo:
            raise ServicioError("Debe especificar el tipo de equipo")

        self._tipo_equipo = tipo_equipo

    def calcular_costo(self, dias: int = 1) -> float:
        if dias <= 0:
            raise ServicioError("Los días deben ser mayores a 0")

        return self._costo_base * dias

    def descripcion(self) -> str:
        return f"Alquiler de equipo tipo: {self._tipo_equipo}"


class ServicioAsesoria(Servicio):
    """Servicio de asesoría especializada"""

    def __init__(self, nombre: str, costo_base: float, especialidad: str):
        super().__init__(nombre, costo_base)

        if not especialidad:
            raise ServicioError("Debe especificar la especialidad")

        self._especialidad = especialidad

    def calcular_costo(self, horas: int = 1, descuento: float = 0) -> float:
        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores a 0")

        if descuento < 0 or descuento > 1:
            raise ServicioError("El descuento debe estar entre 0 y 1")

        total = self._costo_base * horas
        return total * (1 - descuento)

    def descripcion(self) -> str:
        return f"Asesoría en: {self._especialidad}"
    
# =========================
# PRUEBAS DE ERRORES
# =========================

if __name__ == "__main__":
    print("=== INICIANDO PRUEBAS DE SERVICIOS ===\n")

    # 1. ❌ Error: costo negativo
    try:
        s1 = ServicioAsesoria("Asesoria IA", -500, "IA")
    except ServicioError as e:
        print(f"✔ Prueba 1 OK (costo negativo): {e}")

    # 2. ❌ Error: nombre vacío
    try:
        s2 = ServicioSala("", 100, 10)
    except ServicioError as e:
        print(f"✔ Prueba 2 OK (nombre vacío): {e}")

    # 3. ❌ Error: capacidad inválida
    try:
        s3 = ServicioSala("Sala pequeña", 100, 0)
    except ServicioError as e:
        print(f"✔ Prueba 3 OK (capacidad inválida): {e}")

    # 4. ❌ Error: tipo de equipo vacío
    try:
        s4 = ServicioEquipo("Alquiler PC", 200, "")
    except ServicioError as e:
        print(f"✔ Prueba 4 OK (tipo equipo vacío): {e}")

    # 5. ❌ Error: descuento inválido
    try:
        s5 = ServicioAsesoria("Asesoria Cloud", 300, "Cloud")
        s5.calcular_costo(horas=2, descuento=1.5)
    except ServicioError as e:
        print(f"✔ Prueba 5 OK (descuento inválido): {e}")

    # 6. ❌ Error: horas inválidas
    try:
        s6 = ServicioSala("Sala VIP", 100, 10)
        s6.calcular_costo(horas=0)
    except ServicioError as e:
        print(f"✔ Prueba 6 OK (horas inválidas): {e}")

    print("\n=== FIN DE PRUEBAS ===")