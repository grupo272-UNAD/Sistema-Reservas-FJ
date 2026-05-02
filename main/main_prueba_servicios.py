# Se importa las clases y metodos de las partes del trabajo (por el momento solo servicio).
from servicio import Servicio, ServicioError
from logger import registrar_error, registrar_evento

def operacion_crear_servicio(Servicio, datos_del_servicio):
    print(f"\n--- Intentando crear un servicio:{Servicio.__name__} ---")
    try:
        # Se ejecuta el primer metodo para la creacion de servicios
        nuevo_servicio = Servicio(**datos_del_servicio)
        
    except ServicioError as error_especifico:
        # registro para errores de servicios perzonalizado por ServiceError.
        registrar_error(f"Fallo de negocio en: {Servicio.__name__}: {error_especifico}")
        print(f"Operación denegada para {Servicio.__name__}.")
        
    except Exception as error_critico:
        # Precaucion para cualquier error que no sea el 'ServiceError'
        registrar_error(f"Fallo crítico critico en {Servicio.__name__}: {error_critico}")
        
    else:
        # Aviso de que el evento se creo sin problemas y registrado en log.
        registrar_evento(f"Servicio {Servicio.__name__} creado exitosamente.")
        return nuevo_servicio
    
    finally:
        print(f"Finalizado intento de creación para {Servicio.__name__}.")