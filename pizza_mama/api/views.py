from django.shortcuts import render

# Create your views here.

def api(request):
    return render(request, 'pizza_mama/api/api.html')