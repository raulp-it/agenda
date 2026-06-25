from conn import obtener_conexion, cerrar_conexion

def max_id():
    conn = obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)

    with conn.cursor() as cursor:
        cursor.execute("SELECT MAX(codigo) FROM agenda")
        result = cursor.fetchone()
        max_id_value = result[0] if result[0] is not None else 0

    cerrar_conexion(conn)
    return max_id_value

def buscar_id(codigo):
    conn = obtener_conexion()
    if conn is None:
        print("No se pudo establecer la conexión a la base de datos. Saliendo del programa.")
        exit(1)

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM agenda WHERE codigo = %s", (codigo,))
        result = cursor.fetchone()

    cerrar_conexion(conn)
    return result
