import os
import time

# Esta funcion obtiene el ancho y alto de la pantalla para centrar los titulos y menues.
def obtener_tamano_terminal():
    return os.get_terminal_size()    

# Limpia la pantalla de acuerdo al SO anfitrion: 
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Centrar el texto.
def centrar_texto(texto, ancho):
    return texto.center(ancho)

# Hace una pausa de 1 seg para dar tiempo a leer el mensaje en la pantalla.
def aguardar():
    time.sleep(1)

# Usar para partes del menu que aun no estan en linea.
def en_construccion():
    print(f"Modulo en construccion...")
    input(f"Presione ENTER para volver al menu principal.")

# Impresion del encabezado
def imprimir_encabezado(titulo):
    ancho = os.get_terminal_size().columns
    print("=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho)

def alto_ancho_pantalla():
    ancho, alto = os.get_terminal_size()
    return ancho, alto
