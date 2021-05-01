from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory # нужно для multiply form
#For registration user
from django.contrib.auth.forms import UserCreationForm
#For login user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#My imports
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import *

def loginPage(request):
	form = AccountAuthenticationForm(request.POST)
	if form.is_valid():
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)

		if user:
			login(request,user)
			return redirect('home')

	else:
		form = AccountAuthenticationForm()		
	
	context = {'login_form':form}		
	return render(request, 'accounts/login.html', context)

	

def registerPage(request):
	context = {}
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email,password=raw_password )
			login(request,account)
			return redirect('home')
		else:
			context['form'] = form 
	else:
		form = CreateUserForm()


	context['form'] = form
	return render(request, 'accounts/register.html', context)	


def homepage(request):
	customers = Customer.objects.all() 
	orders = Order.objects.all()

	total_orders = orders.count()
	orders_delivered = Order.objects.filter(status="Delivered").count()
	orders_pending = Order.objects.filter(status="Pending").count()

	return render(request,'accounts/home.html',
		{"customers":customers, 
		"orders":orders, 
		"total_orders":total_orders,
		"orders_delivered":orders_delivered,
		"orders_pending":orders_pending,
		}
		)


def products(request):
	products = Product.objects.all()
	return render(request,'accounts/products.html',{"products":products})


def customer(request, pk):
	customer		= Customer.objects.get(id = pk)
	orders			= customer.order_set.all() #Обращаемся к ребенку(Order) и к его родителю (Product)
	orders_c		= orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders) # Filter stuff
	orders = myFilter.qs
	return render(request,'accounts/customer.html',{
		'customer':customer,
		'orders':orders,
		'orders_c':orders_c,
		'myFilter':myFilter,
		})	


def create_order(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order,fields=('product','status'),extra=5) #екстра - количетсов форм
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer}) # Initial вставляет  данные из в форму по умолчанию
	if request.method == 'POST':
		#print('Printing POST method',request)
		formset = OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')


	context = {'formset':formset}
	return render(request, 'accounts/order_form.html',context)


def update_order(request, order_pk):

	order = Order.objects.get(id=order_pk)
	form = OrderForm(instance = order) #instance нужно для того, чтобы в форму вписались данные из БД
	if request.method == 'POST':
		form = OrderForm(request.POST, instance= order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html',context)


def delete_order(request, order_pk):
	order = Order.objects.get(id = order_pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')

	context = {"order":order}
	return render(request, 'accounts/delete.html',context)
