import psycopg2
conn = psycopg2.connect(dbname="capitulo_4_db", user="capitulo_4_user", password="patata")
cursor = conn.cursor()
cursor.execute("INSERT INTO emp VALUES ('7364','HUGO','OFICINISTA', \
                       '7903',date '1980-12-17','800.00',NULL,'20');")
cursor.execute("SELECT * FROM emp;")

print(cursor.fetchone())
print("Funciona!")
