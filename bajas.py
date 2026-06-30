from funciones import limpiar_pantalla, aguardar, imprimir_encabezado
from consultas import buscar_contacto, desactivar_contacto


def menu_bajas():
    titulo = "BAJAS DE CLIENTES"
    while True:
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        codigo = input("Código: ").strip()
        if codigo == '0':
            #cerrar_conexion(conn)
            print("\nVolviendo al menú principal...")
            aguardar()
            break
        if codigo=="":
            input("Codigo ingresado invalido. Presione ENTER para volver a intentar")            
        resultado = buscar_contacto(codigo)        
        if resultado is None:
            print("No se encuentra el codigo\nPresione Enter para continuar")
            continue        
        if resultado[8] == False:
            input("El contacto seleccionado se encuentra desactivado\nPresione Enter para continuar")
            continue
        print("\nContacto a eliminar:")        
        print(f"Codigo: {resultado[0]}")
        print(f"Apellido: {resultado[1]}")
        print(f"Nombre: {resultado[2]}")
        print(f"Direccion: {resultado[3]}")
        print(f"Estado Activo: {resultado[8]}")
        tip_elim=input("Ingrese 'D' para DESACTIVAR cliente o 'E' para ELIMINAR cliente o cualquier otra tecla para cancelar: ").strip().upper()
        confirmar=input("Ingrese 'S' para confirmar la eliminación o desactivación del cliente o cualquier otra tecla para cancelar: ").strip().upper()
        if confirmar != 'S':
            input("\nEliminación cancelada. Presiona Enter para continuar...")
            continue        
        elif tip_elim == 'D':
            desactivar_contacto(codigo)