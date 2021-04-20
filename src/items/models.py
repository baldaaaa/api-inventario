from django.db import models

def upload_location(instance, filename, **kwargs):
    file_path = 'items/{nombre}/{filename}'.format(nombre=instance.nombre,filename=filename)
    return file_path
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nombre

class MiDirectorio(models.Manager):
    def dir_content(self):
        return super(MiDirectorio, self).filter(containing_dir=self.id)

        
class Carpeta(models.Model):
    nombre                  = models.CharField(max_length=50, null=False)
    tags                    = models.ManyToManyField(Etiqueta, blank=True)
    notas                   = models.TextField(max_length=1000, null=True, blank=True)
    containing_dir          = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_main			    	= models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    cantidad = models.IntegerField()
    cantidad_minima = models.IntegerField(default=0)
    precio = models.FloatField(null=True)
    tags = models.ManyToManyField(Etiqueta)
    notas = models.TextField(max_length=1000, null=True, blank=True)
    codigo_qr = models.ImageField(upload_to=upload_location, null=True, blank=True)
    folder = models.ForeignKey(Carpeta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre