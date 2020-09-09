from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.db import connection

def insert(request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO emp VALUES ('7364','HUGO','OFICINISTA', \
                       '7903',date '1980-12-17','800.00',NULL,'20');")
    cursor.execute("select * from emp")
    return HttpResponse('<html> inserted </html>')


def select(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from emp")
        html = '<html>'
        columns = [col[0] for col in cursor.description]
        for column in columns:
            html += str(column) + '|'
        html += '<br>'
        for empleado in cursor.fetchall():
            for columna in empleado:
                html += str(columna) + '|'
            html += '<br>'
        html += '</html>'

    response = HttpResponse(html)
    return response
