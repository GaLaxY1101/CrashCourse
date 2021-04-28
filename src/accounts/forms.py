from django.forms import ModelForm
from .models import Order
#For user register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
	class Meta:
		model 	= Order # модель, к которой мы делаем форму 
		fields 	= '__all__' # или ['field1','field2'] название поолей нужно брнать из модели


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['email','username','password1', 'password1']
