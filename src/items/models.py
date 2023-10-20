from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
from base64 import b64encode

def qr_upload_location(instance, filename, **kwargs):
    file_path = 'qr/{filename}'.format(nombre=instance.nombre,filename=filename)
    return file_path
    

        
class Carpeta(models.Model):
    nombre                  = models.CharField(max_length=50, null=False, blank=False)
    parent_folder           = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug                    = models.SlugField(blank=True, unique=True)
    #tags                    = models.ManyToManyField(Etiqueta, null=True, blank=True)
    notas                   = models.TextField(max_length=1000, null=True, blank=True)
    qr                      = models.ImageField(upload_to=qr_upload_location, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    carpeta                 = models.ForeignKey(Carpeta, on_delete=models.CASCADE)
    nombre                  = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre                  = models.CharField(max_length=255, null=False, blank=False)
    folder                  = models.ForeignKey(Carpeta, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True)
    cantidad                = models.IntegerField(null=False, blank=False)
    cantidad_minima         = models.IntegerField(null=True, blank=True)
    precio                  = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=15)
    tags                    = models.ManyToManyField(Etiqueta)
    notas                   = models.TextField(max_length=1000, null=True, blank=True)
    qr                      = models.ImageField(upload_to=qr_upload_location, null=True, blank=True)
    
    def __str__(self):
        return self.nombre