from django.shortcuts import render
import psycopg2
# Create your views here.

def home(request):
    # Connect to an existing database
    conn = psycopg2.connect("dbname=capitulo_4_db user=capitulo_4_user")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
                 ...(100, "abc'def"))

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM test;")
    cur.fetchone()
    (1, 100, "abc'def")

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO emp VALUES ('7364','HUGO','OFICINISTA', \
                       '7903',date '1980-12-17','800.00',NULL,'20');")

    return HttpResponse('<html> inserted </html>')