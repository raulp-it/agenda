import time
import os
from datetime import date

ancho, alto = os.get_terminal_size()
anio_actual = date.today().year

def presentacion():
    print("\n")   

    separador = "█" 

    texto = f"SCPC Labs: Desarrollos Informáticos - (c) {anio_actual}"
    texto = texto.center(ancho)
    print("\n")
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    print()

    print("\n")
    print(separador*ancho)
    texto = f"Agenda de Contactos v2.0 - Desarrollada por Raul Peralta"
    texto = texto.center(ancho)
    print("\n")
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)

    print("\n\n")
    texto=f"Prohibida su reproducción total o parcial"
    texto = texto.center(ancho)
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    print()

    print("\n")
    print(separador*ancho)

    print("\n\n")
    texto=f"Todos los derechos reservados - Raul Peralta - (c) {anio_actual}"
    texto = texto.center(ancho)
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    