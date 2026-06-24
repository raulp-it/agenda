import os
from funciones import limpiar_pantalla
from conn import obtener_conexion, cerrar_conexion
from funciones import aguardar
#from consultas import max_id

ancho, alto = os.get_terminal_size()
separador = "=" 
titulo = "ALTAS DE CLIENTES"
titulo_centrado = titulo.center(ancho)
def menu_altas():
    while True:
        conn = obtener_conexion()        
        limpiar_pantalla()
        print(separador*ancho)
        print(titulo_centrado)
        print(separador*ancho)        
        print("Ingrese '0' en el campo Código para volver al menú principal...")
        codigo = input("Código: ").strip()
        if codigo == '0':
            cerrar_conexion(conn)
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
        if conn is None:
            print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
            exit(1)
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO agenda (codigo, apellido, nombre, domicilio, cp, email, telefono, localidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (codigo, apellido, nombre, domicilio, cod_postal, email, telefono, localidad)
                )
                conn.commit()
                print("\nRegistro ingresado con éxito. Presiona Enter para continuar...")
                aguardar()
        except Exception as e:
            input(f"Error al insertar el registro: {e}, presiona Enter para continuar...")
        finally:
            cerrar_conexion(conn)
