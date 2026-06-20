import os
import time


def pantalla():
    ancho, alto = os.get_terminal_size()
    return ancho, alto

def obtener_tamano_terminal():
    return os.get_terminal_size()

def limpiar_pantalla():
    # os.name es 'nt' para Windows y 'posix' para Linux/macOS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def centrar_texto(texto, ancho):
    return texto.center(ancho)

def aguardar():
    time.sleep(1)