# EXCEPCIÓN PERSONALIZADA
# =========================================================

class ServicioError(Exception):

    pass


# =========================================================
# CLASE SERVICIO SALA
# =========================================================

class ServicioSala:

    # Constructor
    def __init__(self, nombre, precio, capacidad):

        self.nombre = nombre
        self.precio = precio
        self.capacidad = capacidad

    # Método calcular costo
    def calcular_costo(self, horas):

        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores a 0"
            )

        return self.precio * horas


# =========================================================
# CLASE SERVICIO EQUIPO
# =========================================================

class ServicioEquipo:

    # Constructor
    def __init__(self, nombre, precio, categoria):

        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    # Método calcular costo
    def calcular_costo(self, dias):

        if dias <= 0:

            raise ServicioError(
                "Los días deben ser mayores a 0"
            )

        return self.precio * dias


# =========================================================
# CLASE SERVICIO ASESORIA
# =========================================================

class ServicioAsesoria:

    # Constructor
    def __init__(self, nombre, precio, area):

        self.nombre = nombre
        self.precio = precio
        self.area = area

    # Método calcular costo
    def calcular_costo(self, horas):

        if horas <= 0:

            raise ServicioError(
                "Las horas deben ser mayores a 0"
            )

        return self.precio * horas