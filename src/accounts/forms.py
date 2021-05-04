from django.forms import ModelForm
from .models import Order, Customer
#For user register
from django.contrib.auth.forms import UserCreationForm
from django import forms
#For login
from django.contrib.auth import authenticate



class AccountAuthenticationForm(ModelForm):
	password = forms.CharField(label='Password')
	
	class Meta:
		model = Customer
		fields = ('email','password')

	def clean(self):
		if self.is_valid(): #self = form
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError('Invalid login')


class OrderForm(ModelForm):
	class Meta:
		model 	= Order # модель, к которой мы делаем форму 
		fields 	= '__all__' # или ['field1','field2'] название поолей нужно брнать из модели


class CreateUserForm(UserCreationForm):
	email = forms.EmailField(max_length=60,)

	class Meta:
		model = Customer
		fields = ('email','username','password1', 'password1')
