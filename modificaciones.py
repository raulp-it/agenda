from funciones import obtener_tamano_terminal, imprimir_encabezado
from funciones import limpiar_pantalla
from funciones import aguardar
from consultas import buscar_contacto, activar_contacto, modificar_contacto

ancho, alto = obtener_tamano_terminal()
separador = "=" 
titulo = "MODIFICACION DE DATOS DE CLIENTES"
titulo_centrado = titulo.center(ancho)
def menu_modificaciones():
    while True:        
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        codigo = input("Código: ").strip()
        if codigo == '0' or codigo=="":            
            print("\nVolviendo al menú principal...")
            aguardar()
            break        
        result = buscar_contacto(codigo)
        if result is None:
            print("No se encuentra el codigo")
            break
        limpiar_pantalla()
        print("\nContacto a modificar:")
        print(separador * ancho)
        print(f"{'Código':<7}{'Apellido':<15}{'Nombre':<15}{'Domicilio':<25}{'Activo':<2}")
        print(separador * ancho)
        print(
            f"{result[0]:<7}"
            f"{result[1]:<15}"
            f"{result[2]:<15}"
            f"{result[3]:<25}"
            f"{result[8]:<2}"
        )
        tip_mod=input("Ingrese 'A' para REACTIVAR cliente o 'M' para MODIFICAR cliente o cualquier otra tecla para cancelar: ").strip().upper()
        confirmar=input("Ingrese 'S' para confirmar la MODIFICACION o REACTIVACION del cliente o cualquier otra tecla para cancelar: ").strip().upper()
        if confirmar != 'S':
            input("\nModificación cancelada. Presiona Enter para continuar...")
            continue        
        elif tip_mod == 'A':
            if result[8]==1:
                input("El cliente YA SE ENCUENTRA ACTIVO. Presione ENTER para reintentar.")
                continue
            else:
                activar_contacto(codigo)
        if tip_mod == 'M':
            print("Ingrese los nuevos datos del cliente. Dejar en blanco para mantener el valor actual.")
            new_apellido = input(f"Apellido [{result[1]}]: ").strip() or result[1]
            new_nombre = input(f"Nombre [{result[2]}]: ").strip() or result[2]
            new_domicilio = input(f"Domicilio [{result[3]}]: ").strip() or result[3]
            new_cp = input(f"Codigo Postal [{result[4]}]: ").strip() or result[4]
            new_email = input(f"Email [{result[7]}]: ").strip() or result[7]
            new_telefono = input(f"Telefono [{result[6]}]: ").strip() or result[6]
            new_localidad = input(f"Localidad [{result[5]}]: ").strip() or result[5]
            modificar_contacto(new_apellido, new_nombre, new_domicilio, new_cp, new_email, new_telefono, new_localidad, codigo)
            input("\nPresiona Enter para continuar...")
