from django.shortcuts import render
from jeans.models import Jeans

def home(request):

    data = {
        'Jeans': Jeans.objects.all(),
        'title': 'Головна сторінка'
    }
    return render(request, 'jeans/home.html', data)


def man(request):
    return render(request, 'jeans/man.html')


def woman(request):
    return render(request, 'jeans/woman.html')
