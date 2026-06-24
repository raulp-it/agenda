import psycopg as psycopg_

def obtener_conexion():
    try:
        conn = psycopg_.connect(
            host="localhost",
            port=5432,
            dbname="agenda",
            user="agenda_usr",
            password="SoyLaComadreja"
        )
        print("Conectado a PostgreSQL")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None

def cerrar_conexion(conn):
    if conn is not None:
        conn.close()
        print("Conexión cerrada")

#obtener_conexion()
#cerrar_conexion(obtener_conexion())