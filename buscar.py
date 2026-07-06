from funciones import imprimir_encabezado, limpiar_pantalla, alto_ancho_pantalla, centrar_texto, aguardar
from consultas import buscar_por_nombre, buscar_por_apellido
titulo = "BÚSQUEDA DE CLIENTES"
separador = "="
ancho, alto = alto_ancho_pantalla()

def menu_buscar():
    while True:
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        limpiar_pantalla()
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        print("Ingrese 1 para buscar por nombre: ")
        print("Ingrese 2 para buscar por apellido: ")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            result = buscar_por_nombre(nombre)
        elif opcion == '2':
            apellido = input("Ingrese el apellido del cliente a buscar: ")
            result = buscar_por_apellido(apellido)
        else:
            print("Opción no válida.")
            aguardar()
            return
        limpiar_pantalla()
        print(separador * ancho)
        print(f"{{titulo:^{ancho}}}".format(titulo=titulo))
        print(separador * ancho)        
        print(f"{'Código':<8}{'Apellido':<20}{'Nombre':<22}{'Teléfono':<15}")
        print("_" * ancho)
        for fila in result:            
            print(
            f"{fila[0]:<8}"
            f"{fila[1]:<20}"
            f"{fila[2]:<22}"
            f"{fila[7]:<15}"
            )        
        print("_" * ancho)
        input(f"Presione ENTER para continuar")
        
