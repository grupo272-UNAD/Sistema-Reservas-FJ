"""
Modulo: cliente.py 
Define la estructura de la entidad Cliente y sus reglas de integridad.
Se aplican conceptos de:
- Encapsulación: Uso de atributos privados (__nombre) para proteger los datos.
- Métodos de Acceso: Implementación de decoradores @property para lectura segura.
"""
"""
Modulo: cliente.py 
Define la entidad Cliente con validaciones internas.
"""

class ClienteError(Exception):
    """Excepción personalizada para errores de la clase Cliente."""
    pass

class Cliente:
    def __init__(self, nombre: str, correo: str, id_cliente: str):
        # Validaciones de integridad inmediata
        if not nombre or not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")
        if "@" not in correo:
            raise ClienteError("El formato del correo es inválido.")
        
        self.__nombre = nombre
        self.__correo = correo
        self.__id_cliente = id_cliente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo
    
    @property
    def idCliente(self):
        return self.__id_cliente

