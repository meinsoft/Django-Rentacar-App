from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Carlist

def car_list(request):
    cars = Carlist.objects.all()
    return render(request, 'car_list.html',{'cars':cars})

def car_detail(request, slug):
    return render(request, 'car_detail.html', {'car': get_object_or_404(Carlist, slug=slug)})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')