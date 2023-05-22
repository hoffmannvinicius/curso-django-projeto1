from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Vinicius Hoffmann'})


def contato(request):
    return render(request, 'temp/contato.html')


def sobre(request):
    return render(request)
