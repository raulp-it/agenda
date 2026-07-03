from funciones import imprimir_encabezado
from funciones import limpiar_pantalla
from funciones import aguardar
from consultas import insertar_contacto, buscar_max_id

def menu_altas():
    titulo = "ALTAS DE CLIENTES"
    while True:        
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        print("Presione Enter para asignar automáticamente un código al nuevo cliente.")
        codigo = input("Código: ").strip()
        if codigo == '0':
            print("\nVolviendo al menú principal...")
            aguardar()
            break
        if codigo=="":
            id = buscar_max_id() + 1
            codigo = str(id)
            print(f"Se asignará el código {codigo} al nuevo cliente.")
            print(f"Codigo: {codigo}")
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        cod_postal= input("Código Postal: ")
        if cod_postal == "9999":
            localidad = "Springfield"
            print(f"Localidad: {localidad}")
        else:
            localidad = input("Localidad: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        limpiar_pantalla()
        insertar_contacto(codigo,
                          apellido,
                          nombre,
                          domicilio,
                          cod_postal,
                          email,
                          telefono,
                          localidad)
        print("\nRegistro ingresado con éxito. Presiona Enter para continuar...")
        aguardar()

