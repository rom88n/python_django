from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {
        'title': '! Главная страница',
        'values': ['1', '2', '3'],
        'obj': {
            'car': 'VW',
            'model': 'Tiguan',
            'year': 2017,
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': '! About страница',
    }
    return render(request, 'main/about.html', data)

