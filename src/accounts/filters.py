import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date 		= DateFilter(field_name="date_created", lookup_expr='gte') # GTE means greater or equal(>=)
	#loocup_expresion
	end_date 		= DateFilter(field_name="date_created", lookup_expr='lte') # LTE means less or qual(<=)
	note 			= CharFilter(field_name="note", lookup_expr ='icontains' ) # icontains - ignore case sensetivity
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer','date_created'] # Исключить. То есть все поля кроме customer и date_created
