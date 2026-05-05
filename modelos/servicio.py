# ==========================================
# MODELO SERVICIOS
# ==========================================

class ServicioSala:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad


class ServicioEquipo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo


class ServicioAsesoria:
    def __init__(self, tema, asesor):
        self.tema = tema
        self.asesor = asesor


class ServicioError(Exception):
    pass