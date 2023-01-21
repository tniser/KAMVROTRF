from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    categories = MenuCategory.objects.all()
    names = MenuName.objects.all()
    prices = MenuPrice.objects.all()
   
    context = {
        'categories' : categories,
        'names' : names,
        'prices': prices,
    }

    return render(request, 'contacts/index.html', context)

def hours(request):
    return render(request, 'contacts/hours.html')

def contact_us(request):
    return render(request, 'contacts/contact.html')

def about(request):
    return render(request, 'contacts/about.html')

def thanks(request):
    name = request.GET['name']
    email = request.GET['email']
    text = request.GET['message']

    db_data = Contact(contacts_name = name, contacts_email = email, contacts_text = text)
    db_data.save()

    return render(request, 'contacts/thanks.html', {'name' : name})

def dbinfo(request):
    db_data1 = MenuCategory.objects.all()
    db_data2 = MenuName.objects.all()
    db_data3 = MenuPrice.objects.all()

    return render(request, 'contacts/dbinfo.html', {'db_data1' : db_data1, 'db_data2' : db_data2, 'db_data3' : db_data3,})