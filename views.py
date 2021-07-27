from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Order

from django.contrib import messages
import datetime

global thank  #Sem isto tinhamos um erro de local storage
global id



def index(request) :
    return render(request,"index.html")

def services(request) :
    return HttpResponse("services")

def contact(request) :

    #Faz um model de database no "model.py" por nome...
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.date.today())
        contact.save()
        messages.success(request, 'Form Submitted!')
    return render(request,"contact.html")

def me(request) :
    return render(request,"about.html")

def quizz(request):
    return render(request,"quizz.html")


def quizz_resultados(request):
    if request.method == "POST":

        pontuacao = 0

        print(request.POST)

        if request.POST["q1"] == "1970":
            pontuacao += 10
        if request.POST["q2"] == "boom":
            pontuacao += 10
        if request.POST["q3"] == "azul":
            pontuacao += 10
        if request.POST["q4"] == "15":
            pontuacao += 10
        if request.POST["q5"] == "sudoeste":
            pontuacao += 10
        if request.POST["q6"] == "nosalive":
            pontuacao += 10
        if request.POST["q7"] == "roskilde":
            pontuacao += 10
        # if request.POST["q8"] == "1970":
        #	pontuacao += 10
        # if request.POST["q9"] == "1970":
        #	pontuacao += 10
        # if request.POST["q10"] == "1970":
        #	pontuacao += 10

        return render(request, 'quizz_resultados.html', {
            "pontuacao": pontuacao,
            "q1": request.POST["q1"],
            "q2": request.POST["q2"],
            "q3": request.POST["q3"],
            "q4": request.POST["q4"],
            "q5": request.POST["q5"],
            "q6": request.POST["q6"],
            "q7": request.POST["q7"]  # ,
            # "q8": request.POST["q8"],
            # "q9": request.POST["q9"],
            # "q10": request.POST["q10"]
        })

    return HttpResponseBadRequest()

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        order= Order(amount=amount,items_json=items_json,name=name, email=email, phone=phone, address=address,city=city,zip_code=zip_code,state=state)
        order.save()
        thank = True

        id = order.order_id
        return render(request,"checkout.html",  {'thank': thank, 'id': id})
    return render(request, "checkout.html")

def sobre(request):
    return render(request,"sobre.html")