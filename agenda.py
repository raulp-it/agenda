from presenta import presentacion
from funciones import limpiar_pantalla
from funciones import aguardar
from funciones import obtener_tamano_terminal
from funciones import centrar_texto
from acerca import menu_acerca

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
        print("\t6. Acerca de este proyecto")
        
        opcion = input("\nSelecciona una opción: ")
        if opcion == '1':    
            print("Altas de Clientes")
            limpiar_pantalla()
            #menu_altas()
            limpiar_pantalla()
        elif opcion == '2':
            limpiar_pantalla()
            print("Bajas de Clientes")
            limpiar_pantalla()
            #menu_bajas()
            limpiar_pantalla()
        elif opcion == '3':
            print("Modificación de Clientes")
            limpiar_pantalla()
            #menu_presupuestos()
            limpiar_pantalla()
        elif opcion == '4':
            print("Listado de Clientes")
            limpiar_pantalla()
            #menu_listado()
            limpiar_pantalla()
        elif opcion == '5':
            print("Imprimir Listado")
            limpiar_pantalla()
            #menu_imprimir()
            limpiar_pantalla()
        elif opcion == '6':
            print("Acerca de este proyecto")
            limpiar_pantalla()
            menu_acerca()
            limpiar_pantalla()
        elif opcion == '0':
            print("Saliendo del programa...")
            limpiar_pantalla()
            break
        else:            
            print("Opción no válida, por favor selecciona una opción del 0 al 6.")
            input("\nPresiona Enter para continuar...")
            limpiar_pantalla()

menu_principal()