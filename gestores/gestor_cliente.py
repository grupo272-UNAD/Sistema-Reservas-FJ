
from cliente import Cliente, ClienteError

class GestorCliente:
    def __init__(self):
        self.__clientes = []

    def registrar_cliente(self, cliente: Cliente):
        try:
            # Verificacion de cliente si ya existe
            self.__clientes.append(cliente)
            self._log(f"Cliente registrado: {cliente.nombre} | ID: {cliente.id_cliente} | Correo: {cliente.correo}")
        except Exception as e:
            self._log(f"Error al registrar cliente: {str(e)}")

    def buscar_cliente(self, id_cliente):
        for c in self.__clientes:
            if c.id_cliente == id_cliente:
                return c
        return None

    def _log(self, mensaje):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[CLIENTE]: {mensaje}\n")