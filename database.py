import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='0911',
    host='localhost',
    database='postgres'
)

conn.autocommit=True

cursor = conn.cursor()
cursor.execute("CREATE DATABASE proyecto5")
print("Base de datos creada")
cursor.close()
conn.close()
