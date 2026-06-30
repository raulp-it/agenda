from funciones import imprimir_encabezado
from funciones import limpiar_pantalla
from funciones import aguardar
from consultas import insertar_contacto

def menu_altas():
    titulo = "ALTAS DE CLIENTES"
    while True:        
        limpiar_pantalla()
        imprimir_encabezado(titulo)
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        codigo = input("Código: ").strip()
        if codigo == '0' or codigo=="":
            print("\nVolviendo al menú principal...")
            aguardar()
            break
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        domicilio = input("Domicilio: ")
        cod_postal= input("Código Postal: ")
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

