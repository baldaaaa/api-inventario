from django.shortcuts import render

def index_view(request):
    context = {}
    return render(request, 'index.html', context)

def como_funciona_view(request):
    context = {}
    return render(request, 'comofunciona.html', context)

def contacto_view(request):
    context = {}
    return render(request, 'contacto.html', context)

def faqs_view(request):
    context = {}
    return render(request, 'faqs.html', context)

def login_view(request):
    context = {}
    return render(request, 'login.html', context)

def precios_view(request):
    context = {}
    return render(request, 'precios.html', context)