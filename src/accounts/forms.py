from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
	class Meta:
		model 	= Order # модель, к которой мы делаем форму 
		fields 	= '__all__' # или ['field1','field2'] название поолей нужно брнать из модели

