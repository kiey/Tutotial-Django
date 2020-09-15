from django.shortcuts import redirect, render

# Create your views here.
def vista_principal(request):
    return render(request, 'home.html')
def vista_anadir(request):
    Item.objects.create(text=request.POST['item_text'], list=list_)

    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")

    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp VALUES ('7365','HUGO','OFICINISTA', \
                   '7903',date '1980-12-17','800.00',NULL,'20');")
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse("Insertado")
    return redirect('home')
