from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

	return render(request,'accounts/customer.html',{
		'customer':customer,
		'orders':orders,
		'orders_c':orders_c,
		})	

def create_order(request):

	form = OrderForm() 
	if request.method == 'POST':
		#print('Printing POST method',request)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}
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
