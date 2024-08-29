from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.



def index(request):
    pizzas = Pizza.objects.all()
    pizzas_names_prices = [pizzas.name + " : " + str(pizzas.price) + "$" for pizzas in pizzas]
    pizzas_names_prices_str = ', '.join(pizzas_names_prices)
    return HttpResponse(f"Pizzas : {pizzas_names_prices_str}")
