from gestores.gestor_cliente import GestorCliente
from gestores.gestor_reserva import GestorReserva
from gestores.gestor_servicio import GestorServicio
from modelos.liente import Cliente, ClienteError
from modelos.servicio import ServicioSala, ServicioEquipo, ServicioAsesoria, ServicioError
from modelos.reserva import Reserva, ReservaError

def inicializar_log():
    with open("logs.txt", "w", encoding="utf-8") as f:
        f.write("=== INICIO DE SIMULACIÓN SOFTWARE FJ ===\n")

def registrar_evento_log(mensaje: str):
    try:
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[Main]: {mensaje}\n")
    except Exception as e:
        print(f"Error crítico: No se pudo escribir en el log. Detalle: {e}")

# metodo para la simulacion o las pruebas de las 10 operaciones
def ejecutar_prueba():
    inicializar_log()
    
    # Intancia de los gestores para base de datos propia.
    gc = GestorCliente()
    gs = GestorServicio()
    gr = GestorReserva()

    print("\n--- Iniciando pruebas ---\n")

    # Operacion 1: Registro de Cliente Válido
    try:
        nuevo_cliente = Cliente("Nose", "Nose@gmail.com", "ID-001")
        gc.registrar_cliente(nuevo_cliente)
        print("[OK] Operación 1: Cliente registrado con éxito.")
    except ClienteError as e:
        print(f"[FALLO] Operación 1: No debería haber fallado. Error: {e}")

    # operacion 2: Registro de cliente invalido
    try:
        print("[INFO] Intentando registrar cliente con correo inválido...")
        cliente_erroneo = Cliente("Usuario Error", "correo_sin_arroba", "ID-555")
        gc.registrar_cliente(cliente_erroneo)
    except ClienteError as e:
        error_msg = f"Operación 2 fallida - Motivo: {e}"
        print(f"[CONTROLADO] {error_msg}")
        registrar_evento_log(error_msg)
    except Exception as e:
        print(f"[CRÍTICO] Operación 2: Error no esperado de tipo {type(e).__name__}")
        
    # Operacion 3: Registro de servicio de asesoria
    # Validar el registro con un servicio especifico
    try:
        # 
        asesoria_ia = ServicioAsesoria("Asesoria IA", 500.0, "IA")
        gs.registrar_servicio(asesoria_ia)
        print(f"[OK] Operación 3: Servicio '{asesoria_ia.nombre}' disponible.")
    except ServicioError as e:
        print(f"[FALLO] Operación 3: Error en servicio: {e}")
        
    # Operacion 4: Registro de servicio de sala erronea
    try:
        print("[INFO] Intentando registrar Servicio de sala con capacidad 0")
        asesoria_sala_erronea = ServicioSala('Sala peque', 100.0, 0 )
        gs.registrar_servicio(asesoria_sala_erronea)
    except ServicioError as e:
        error_msg = f"Operación 4 fallida - Motivo: {e}"
        print(f"[CONTROLADO] {error_msg}")
        registrar_evento_log(error_msg)
    except Exception as e:
        print(f"[CRÍTICO] Operación 4: Error no esperado de tipo {type(e).__name__}")

if __name__ == "__main__":
    try:
        ejecutar_prueba()
    except KeyboardInterrupt:
        print("\nSimulación interrumpida por el usuario.")
    except Exception as e:
        print(f"Error catastrófico en el orquestador: {e}")