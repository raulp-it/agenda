import os
from funciones import limpiar_pantalla

ancho, alto = os.get_terminal_size()
separador = "=" 
titulo = "ALTAS DE CLIENTES"
titulo_centrado = titulo.center(ancho)
def menu_altas():
    while True:
        limpiar_pantalla()
        print(separador*ancho)
        print(titulo_centrado)
        print(separador*ancho)        
        print("Ingrese '0' en el campo Código para volver al menú de artículos.")
        codigo = input("Código: ").strip()
        if codigo == '0':
            break
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        cod_postal= input("Código Postal: ")
        localidad = input("Localidad: ")
        email = input("Email: ")                
        print("\nCliente ingresado con éxito:")
        print(f"Codigo: {codigo}")
        print(f"Apellido: {apellido}")
        print(f"Nombre: {nombre}")
        print(f"Domicilio: {domicilio}")
        print(f"Código Postal: {cod_postal}")
        print(f"Localidad: {localidad}")
        print(f"Email: {email}")
        input("\nPresiona Enter para continuar...")
