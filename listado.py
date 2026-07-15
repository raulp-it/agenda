from funciones import limpiar_pantalla, imprimir_encabezado, alto_ancho_pantalla
from consultas import listar_contactos

titulo = "LISTADO DE CLIENTES"
separador = "="
ancho, alto = alto_ancho_pantalla()
def menu_listado():
    while True:
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        print("O ingrese valores vacios para listar todos los clientes.")
        cod_des = input(f"Código Desde: ").strip()
        if cod_des == '0':
            print("\nVolviendo al menú principal...")            
            break
        cod_has = input(f"Codigo Hasta:").strip() 
        if not cod_des and not cod_des:            
            cod_des = '1'
            cod_has = '999999'
        if not cod_has:
            cod_has=cod_des
        result= listar_contactos(cod_des, cod_has)
        limpiar_pantalla()
        if result is None:
            print("No se encuentra el codigo")
            break
        limpiar_pantalla()
        print(separador * ancho)
        print(f"{{titulo:^{ancho}}}".format(titulo=titulo))
        print(separador * ancho)        
        print(f"{'Código':<8}{'Apellido':<20}{'Nombre':<28}{'Teléfono':<15}")
        print("_" * ancho)
        for fila in result:
            print(
            f"{fila[0]:<8}"
            f"{fila[1]:<20}"
            f"{fila[2]:<28}"
            f"{fila[7]:<15}"
        )
        print("_" * ancho)
        input(f"Presione ENTER para continuar")
            