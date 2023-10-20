from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from cuentas.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(
		max_length=254,
		help_text='Obligatorio. Agrega una cuenta valida.',
	)

	class Meta:
		model = Account
		fields = ('email', 'full_name', 'password1', 'password2', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Ya existe una cuenta registrada con el correo "%s"' % email)

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("No reconocemos ninguna cuenta con esa combinación de correo y contraseña. Intenta de nuevo.")