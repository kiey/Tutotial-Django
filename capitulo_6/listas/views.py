from django.shortcuts import redirect, render
from django.http import HttpResponse
import psycopg2
import psycopg2.extras
import pprint

# Create your views here.
def vista_principal(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    prioridad = request.GET.get('get_prioridad', default='%')
    if prioridad == 'todas':
        prioridad = '%'
    cursor.execute(F"SELECT * FROM Nota WHERE prioridad LIKE '{prioridad}';")

    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'home.html', params)


def vista_principal_(request):
    prioridad = request.GET['get_prioridad']
    return HttpResponse(pprint.pformat(request.GET.keys()))


def vista_principal_endchapter(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    prioridad = request.GET.get('get_prioridad', None)
    print(f"SELECT * FROM Nota WHERE prioridad = '{prioridad}';)")
    cursor.execute(f"SELECT * FROM Nota WHERE prioridad = '{prioridad}';")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    print(request.GET.get('prioridad', None))
    params = {'notas': result, 'get_prioridad': request.GET.get('prioridad', None)}
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











