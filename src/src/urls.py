from django.contrib import admin
from django.urls import path, include
from general.views import busqueda, dashboard, precios_view, contacto_view, items, login_view, logout_view, busqueda, register_view

urlpatterns = [
    # third party
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # general
    path('', dashboard, name='dashboard'),
    path('precios/', precios_view, name='precios'),
    path('contacto/', contacto_view, name='contacto'),
    path('items/', items, name='items'),
    path('busqueda/', busqueda, name='busqueda'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name="deslog"),
    path('registro/', register_view, name='register_view')
]
