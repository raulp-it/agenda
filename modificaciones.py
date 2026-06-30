from funciones import obtener_tamano_terminal
from funciones import limpiar_pantalla
from conn import obtener_conexion, cerrar_conexion
from funciones import aguardar
from consultas import buscar_contacto, desactivar_contacto

ancho, alto = obtener_tamano_terminal()
separador = "=" 
titulo = "MODIFICACION DE DATOS DE CLIENTES"
titulo_centrado = titulo.center(ancho)
def menu_modificaciones():
    while True:
        #conn = obtener_conexion()
        limpiar_pantalla()
        print(separador*ancho)
        print(titulo_centrado)
        print(separador*ancho)
        print()
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        codigo = input("Código: ").strip()
        if codigo == '0' or codigo=="":
            #cerrar_conexion(conn)
            print("\nVolviendo al menú principal...")
            aguardar()
            break        
        resultado = buscar_contacto(codigo)
        if resultado is None:
            print("No se encuentra el codigo")
            break
        print("\nContacto a modificar:")        
        print(f"Codigo: {resultado[0]}")
        print(f"Apellido: {resultado[1]}")
        print(f"Nombre: {resultado[2]}")
        print(f"Direccion: {resultado[3]}")
        print(f"Estado Activo: {resultado[6]}")
        tip_elim=input("Ingrese 'D' para DESACTIVAR cliente o 'E' para ELIMINAR cliente o cualquier otra tecla para cancelar: ").strip().upper()
        confirmar=input("Ingrese 'S' para confirmar la eliminación o desactivación del cliente o cualquier otra tecla para cancelar: ").strip().upper()
        if confirmar != 'S':
            input("\nEliminación cancelada. Presiona Enter para continuar...")
            continue        
        elif tip_elim == 'D':
            desactivar_contacto(codigo)