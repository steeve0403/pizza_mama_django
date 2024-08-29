from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
from django.core import serializers
# Create your views here.



def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_prices = [pi zzas.name + " : " + str(pizzas.price) + "$" for pizzas in pizzas]
    pizzas_names_prices_str = ', '.join(pizzas_names_prices)
    return HttpResponse(f"Pizzas : {pizzas_names_prices_str}")"""
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas })

def api_get_pizza(request):
    pizzas = Pizza.objects.all().order_by('price')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json, content_type="application/json")