import time
from datetime import date
from funciones import limpiar_pantalla, obtener_tamano_terminal, centrar_texto

ancho, alto = obtener_tamano_terminal()
anio_actual = date.today().year

def presentacion():
    print("\n")
    limpiar_pantalla()

    separador = "█" 

    texto = f"SCPC Labs: Desarrollos Informáticos - (c) {anio_actual}"
    texto = centrar_texto(texto, ancho)
    print("\n")
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    print()

    print("\n")
    print(separador*ancho)
    texto = f"Agenda de Contactos v2.0 - Desarrollada por Raul Peralta"
    texto = centrar_texto(texto, ancho)
    print("\n")
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)

    print("\n\n")
    texto=f"Se permite su uso bajo licencia MIT"
    texto2=f"para fines educativos y de investigación"
    texto = centrar_texto(texto, ancho)
    texto2 = centrar_texto(texto2, ancho)
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    print()
    for letra in texto2:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    print()

    print("\n")
    print(separador*ancho)

    print("\n\n")
    texto=f"Todos los derechos reservados - Raul Peralta - (c) {anio_actual}"
    texto = centrar_texto(texto, ancho)
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.025)
    