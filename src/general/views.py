from django.shortcuts import render, redirect
from django.contrib.auth import login, logout ,authenticate
from items.models import Carpeta
from cuentas.forms import RegistrationForm, AccountAuthenticationForm

def dashboard(request):
    
    user = request.user
    if not user.is_authenticated:
        return redirect('login_view')

    # default_folder = Carpeta.objects.filter(is_root=True)
    # context = {
    #     'folders': default_folder,
    # }

    return render(request, 'dashboard.html')

def busqueda(request):
    context = {}
    return render(request, 'comofunciona.html', context)

def contacto_view(request):
    context = {}
    return render(request, 'contacto.html', context)

def items(request):

    user = request.user
    if not user.is_authenticated:
        return redirect('login_view')

    root = MiDashboard.objects.get(usuario=user).root
    try:
        current_folder = request.session['current_folder']
        if current_folder.slug is not root.slug:
            #redirect to localhost/carpeta/{id}/blabla
            print('hola')
        else:
            request.session['current_folder'] = root
    except KeyError:
        request.session['current_folder'] = root

    context = {
        'root': root,
    }

    return render(request, 'items.html', context)

#def create_folder(): this needs ajax

def register_view(request, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
        
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            #first_name = form.cleaned_data['first_name']
            cuenta = authenticate(email=email, password=raw_password)
            #send_registration_mail(email, first_name)
            login(request, cuenta)
            return redirect('dashboard')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registro.html', context)

def login_view(request):
    context = {}
    
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')

    # try:
    #     next_page = request.GET.get("next")
    # except:
    #     next_page = None
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            cuenta = authenticate(email=email, password=password)
            
            if cuenta:
                login(request, cuenta)
                return redirect('dashboard')
    else:
        form = AccountAuthenticationForm()
        
    context['login_form'] = form

    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')

def precios_view(request):
    context = {}
    return render(request, 'precios.html', context)