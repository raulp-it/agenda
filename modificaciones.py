from funciones import obtener_tamano_terminal, imprimir_encabezado
from funciones import limpiar_pantalla
from funciones import aguardar
from consultas import buscar_contacto, activar_contacto

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
        tip_mod=input("Ingrese 'A' para REACTIVAR cliente o 'M' para ELIMINAR cliente o cualquier otra tecla para cancelar: ").strip().upper()
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