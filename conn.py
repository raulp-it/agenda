import psycopg2 as psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="agenda",
        user="agenda_user",
        password="SoyLaComadreja"
    )

    print("Conectado a PostgreSQL")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals():
        conn.close()