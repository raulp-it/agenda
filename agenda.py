from presenta import presentacion
from funciones import limpiar_pantalla, aguardar, obtener_tamano_terminal, centrar_texto
from acerca import menu_acerca
from altas import menu_altas
from bajas import menu_bajas
from listado import menu_listado
from modificaciones import menu_modificaciones
from imprimir import menu_imprimir
from buscar import menu_buscar

# Llama a la función cuando necesites borrar la consola
limpiar_pantalla()
presentacion()
aguardar()
limpiar_pantalla()

ancho, alto = obtener_tamano_terminal()
separador = "=" 
titulo = "A G E N D A  DE  C L I E N T E S v2.0"
titulo_centrado = centrar_texto(titulo, ancho)
menu_principal_centrado = centrar_texto("** Menu Principal **", ancho)
def menu_principal():
    while True:
        print(separador*ancho)
        print(titulo_centrado)
        print(separador*ancho)
        print(menu_principal_centrado)
        print("\t0. Cerrar programa")
        print("\t1. Altas de Clientes")
        print("\t2. Bajas de Clientes")
        print("\t3. Modificar Clientes")
        print("\t4. Listado de Clientes")
        print("\t5. Imprimir Listado")
        print("\t6. Buscar Clientes")
        print("\t7. Acerca de este proyecto")
        opcion = input("\nSelecciona una opción: ")
        if opcion == '1':
            # Alta de Contactos
            limpiar_pantalla()
            menu_altas()
            limpiar_pantalla()
        elif opcion == '2':
            # Baja de Contactos
            limpiar_pantalla()
            menu_bajas()
            limpiar_pantalla()
        elif opcion == '3':
            # Modificacion de Contactos
            limpiar_pantalla()
            print(f"Modificacion de Contactos")
            #en_construccion()
            menu_modificaciones()
            limpiar_pantalla()
        elif opcion == '4':
            # Listado Contactos
            limpiar_pantalla()
            menu_listado()
            limpiar_pantalla()
        elif opcion == '5':
            # Imprimir de Contactos
            limpiar_pantalla()
            menu_imprimir()
            limpiar_pantalla()
        elif opcion == '6':
            # Buscar Contactos
            print("Buscando Contactos...")
            # en_construccion()
            menu_buscar()
            limpiar_pantalla()
        elif opcion == '7':
            # Acerca de
            print("Acerca de este proyecto")
            limpiar_pantalla()
            menu_acerca()
            limpiar_pantalla()
        elif opcion == '0':
            print("Saliendo del programa...")
            limpiar_pantalla()
            break
        else:
            print("Opción no válida, por favor selecciona una opción del 0 al 7.")
            input("\nPresiona Enter para continuar...")
            limpiar_pantalla()

menu_principal()
