from django.contrib import admin
from django.urls import path, include
from general.views import index_view, precios_view, contacto_view, faqs_view, login_view, como_funciona_view

urlpatterns = [
    # third party
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # general
    path('', index_view, name='index'),
    path('precios/', precios_view, name='precios'),
    path('contacto/', contacto_view, name='contacto'),
    path('faqs/', faqs_view, name='faqs'),
    path('como-funciona/', como_funciona_view, name='como-funciona'),
    path('login/', login_view, name='ingresa')
]
