from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from items.models import Carpeta


#######                  ACCOUNTS & DATABASES

INDUSTRY_CHOICES = (
	('Industrial/Manufactura','Industrial/Manufactura'),
	('Contabilidad','Contabilidad'),
)

FUNCION_CHOICES = (
	('Administrativo','Administrativo'),
	('Legal','Legal'),
	('Ingenieria','Ingenieria'),
	('Marketing/Ventas','Marketing/Ventas'),
)

ROL_CHOICES = (
	('Titular','Titular'),
	('Manager','Manager'),
	('Miembro del Equipo','Miembro del Equipo'),
	('Consumidor','Consumidor'),
)


class MyAccountManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError('Este es un campo requerido')
		if not full_name:
			raise ValueError('Este es un campo requerido')

		user = self.model(
			email=self.normalize_email(email),
			full_name=full_name,

		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			full_name=full_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	full_name				= models.CharField(max_length=255)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	class Meta:
		verbose_name_plural = 'Usuarios'

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserProfile(models.Model):
	user 					= models.OneToOneField(Account, on_delete=models.CASCADE)
	job_function			= models.CharField(max_length=50, choices=FUNCION_CHOICES, default=FUNCION_CHOICES[0])
	team_role				= models.CharField(max_length=50, choices=ROL_CHOICES, default=ROL_CHOICES[0])
	telephone_number		= models.CharField(max_length=15, null=True, blank=False)

    # Add any other user-specific fields you need
	
	def __str__(self):
		return self.user.full_name

class Company(models.Model):
	user 				= models.OneToOneField(Account, on_delete=models.CASCADE)
	nombre 				= models.CharField(max_length=50)
	carpeta				= models.OneToOneField(Carpeta, on_delete=models.CASCADE)
	industria 			= models.CharField(max_length=100, null=True, choices=INDUSTRY_CHOICES)
	color_compania 		= models.CharField(max_length=7, default='#FFFFFF')

	def __str__(self):
		return self.nombre


# class Team(models.Model):
# 	company_name 	= models.ForeignKey(Company, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.company_name