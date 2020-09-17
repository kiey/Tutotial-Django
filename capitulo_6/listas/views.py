from django.shortcuts import redirect, render
from django.http import HttpResponse
import psycopg2
import psycopg2.extras

# Create your views here.
def vista_principal(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM Nota;")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'home.html', params)


def vista_principal_(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor.execute("SELECT * FROM Nota;")
    result = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    params = {'nota': result}
    return render(request, 'home.html', params)

def vista_anadir(request):

    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Nota VALUES ('{prioridad}','{titulo}','{nota}');")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('home')


"""
return(HttpResponse(f'Insertado <br> '
                    f'prioridad: {prioridad}<br>'
                    f'titulo: {titulo}<br>'
                    f'nota: {nota}'))

"""











