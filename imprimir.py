from funciones import limpiar_pantalla, imprimir_encabezado, alto_ancho_pantalla
from consultas import mostrar_listado

titulo="IMPRESION DE LISTADO POR PANTALLA"

ancho, alto = alto_ancho_pantalla()
separador = "="
def menu_imprimir():
    while True:
        limpiar_pantalla()
        imprimir_encabezado(titulo)        
        var=input(f"\nPresione ENTER para imprimir \n" \
                  "o '0' para volver al menu principal: ")
        if var=='0':
            break
        if var=="":
            contador = 1
            pagina = 1
            result = mostrar_listado()
            limpiar_pantalla()
            print(separador * ancho)
            print(f"{'Código':<7}{'Apellido':<15}{'Nombre':<22}{'Domicilio':<25}{'Teléfono':<10}")
            print(separador * ancho)
            for fila in result:
                print(
                    f"{fila[0]:<7}"
                    f"{fila[1]:<15}"
                    f"{fila[2]:<22}"
                    f"{fila[3]:<25}"
                    f"{fila[7]:<10}"                    
                )
                contador +=1
                if contador==alto:
                    print(f"Cont = {contador}")
            input(f"Pagina: {pagina}. Presione ENTER para continuar.")