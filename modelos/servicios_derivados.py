"""
Clases concretas de servicios.
Cada servicio tiene su propia forma de calcular el costo.
"""

from modelos.servicio import Servicio

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.tarifa * horas


class AlquilerEquipo(Servicio):
    def calcular_costo(self, horas):
        # 10% adicional
        return self.tarifa * horas * 1.1


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        # 25% adicional
        return self.tarifa * horas * 1.25