from funciones import limpiar_pantalla, aguardar, imprimir_encabezado, alto_ancho_pantalla
from consultas import listar_contactos

titulo = "LISTADO DE CLIENTES"
separador = "="
ancho, alto = alto_ancho_pantalla()
def menu_listado():
    while True:
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        cod_des = input(f"Código Desde: ").strip()
        if cod_des == '0' or not cod_des:
            print("\nVolviendo al menú principal...")
            aguardar()
            break
        cod_has = input(f"Codigo Hasta:").strip()
        if not cod_has:
            cod_has=cod_des
        result= listar_contactos(cod_des, cod_has)        
        if result is None:
            print("No se encuentra el codigo")
            break
        print(separador * ancho)
        limpiar_pantalla()
        print(f"{'Código':<8}{'Apellido':<20}{'Nombre':<20}{'Teléfono':<15}")
        print("=" * ancho)
        for fila in result:
            print(
            f"{fila[0]:<8}"
            f"{fila[1]:<20}"
            f"{fila[2]:<20}"
            f"{fila[7]:<15}"
        )
        print("=" * ancho)
        input(f"Presione ENTER para continuar")
            