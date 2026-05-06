# Importar excepciones 
from utilidades.excepciones import DatoNoValidoError

# 2. Luego, dentro de la clase...
def registrar_servicio(self, servicio):
    try:
        # Validación de objeto nulo 
        #Error servicio
        if servicio is None:
            raise ServicioError("El servicio no puede ser None")

        # NUEVA VALIDACIÓN 
        #error precio 
        # Verificamos si el precio es negativo o cero
        if servicio.precio <= 0:
            raise DatoNoValidoError(f"El precio ({servicio.precio}) debe ser un valor positivo")
            
        self._servicios.append(servicio)
        self._log(f"Servicio {servicio.nombre} registrado.")

    except (ServicioError, DatoNoValidoError) as e:
        self._log(f"Error: {str(e)}")
        # Importante: relanzamos para que la interfaz sepa que hubo un error
        raise e