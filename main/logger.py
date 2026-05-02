import logging

logging.basicConfig(
    filename='logs.txt',      # Nombre del archivo donde se guardan todo
    level=logging.DEBUG,                 # Registro de los errores.
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato para el registro.
    filemode='a'                         
)

def registrar_error(mensaje):
    # Es un registro para los errores criticos.
    logging.error(mensaje)

def registrar_evento(mensaje):
    # Este es el registro para errores normales.
    logging.info(mensaje)