from conn import obtener_conexion, cerrar_conexion

# Busqueda de cliente por codigo de cliente.
def buscar_contacto(codigo):
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT codigo, apellido, nombre, "\
                    "domicilio, cp, localidad, telefono, email, activo "\
                        "FROM age_base WHERE codigo = %s",
                (codigo,)
            )
            return cursor.fetchone()
    finally:
        cerrar_conexion(conn)

# Eliminacion de cliente por codigo de cliente.
def eliminar_contacto(codigo):
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM age_base WHERE codigo = %s",
                (codigo,)
            )
            conn.commit()
    except Exception as e:
        input(f"Error al intentar eliminar el registro {e}. Presione ENTER para salir.")
    finally:
        cerrar_conexion(conn)

# Desactivar cliente por codigo de cliente.
def desactivar_contacto(codigo):
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE age_base SET activo = FALSE WHERE codigo = %s",
                (codigo,)
            )
            conn.commit()
    except Exception as e:        
        input(f"Error al desactivar el registro: {e}, \
              presiona Enter para continuar...")
    finally:
        cerrar_conexion(conn)

# Cliente previamente desactivado por codigo de cliente.
def activar_contacto(codigo):
    conn = obtener_conexion()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "UPDATE age_base SET activo = TRUE WHERE codigo = %s",
                (codigo,)
            )
            conn.commit()
    except Exception as e:        
        input(f"Error al activar el registro: {e}, \
              presiona Enter para continuar...")
    finally:
        cerrar_conexion(conn)

# Crear nuevo registro de cliente.
def insertar_contacto(codigo,
                      apellido,
                      nombre,
                      domicilio,
                      cod_postal,
                      email,
                      telefono,
                      localidad,
                      ):
    conn=obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO age_base (codigo, apellido, 
                nombre, domicilio, cp, email, telefono, 
                localidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                    (codigo,                     
                     apellido,
                     nombre,
                     domicilio,
                     cod_postal,
                     email,
                     telefono,
                     localidad)
            )
            conn.commit()
    except Exception as e:            
            input(f"Error al insertar el registro: {e}, presiona Enter para continuar...")
    finally:
        cerrar_conexion(conn)

# Listado de cliente por codigo de cliente.
def listar_contactos(cod_des, cod_has):
    conn=obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT codigo, apellido, nombre, domicilio,
                cp, email, activo, telefono, localidad from age_base
                where id >=%s and id <=%s order by codigo::INTEGER asc;
                """,
                (cod_des,
                 cod_has)
                )
            return cursor.fetchall()            
    except Exception as e:
        input(f"No se pudo realizar la consulta. Pulse ENTER para continuar")
    finally:
        cerrar_conexion(conn)
    

def mostrar_listado():
    conn=obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT codigo, apellido, nombre, domicilio,
                cp, email, activo, telefono, localidad from age_base
                order by id::INTEGER asc;
                """
                )
            return cursor.fetchall()            
    except Exception as e:
        input(f"No se pudo realizar la consulta. Pulse ENTER para continuar")
    finally:
        cerrar_conexion(conn)

def modificar_contacto(new_apellido, new_nombre, new_domicilio, new_cp, new_email, new_telefono, new_localidad, codigo):
    conn=obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE age_base
                SET apellido = %s,
                    nombre = %s,
                    domicilio = %s,
                    cp = %s,
                    email = %s,
                    telefono = %s,
                    localidad = %s
                WHERE codigo = %s
                """,
                (new_apellido, new_nombre, new_domicilio, new_cp, new_email, new_telefono, new_localidad, codigo)
            )
            conn.commit()
    except Exception as e:            
            input(f"Error al modificar el cliente: {e}, presiona Enter para continuar...")
    finally:
        cerrar_conexion(conn)

def buscar_max_id():
    conn=obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT MAX(id) FROM age_base;
                """
                )
            return cursor.fetchone()[0]            
    except Exception as e:
        input(f"No se pudo realizar la consulta. Pulse ENTER para continuar")
    finally:
        cerrar_conexion(conn)