from django.db import models

class Customer(models.Model):
	name					= models.CharField(max_length = 50)
	email 					= models.EmailField(max_length = 250)
	phone_number 			= models.CharField(max_length = 12)
	date_created			= models.DateTimeField(auto_now_add = True ,null = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"




class Tag(models.Model):
	name 				= models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name




class Product(models.Model):
	CATEGORY = (
		('Indoor','Indoor'),
		('Out door','Outdoor'),
		)

	name 				= models.CharField(max_length = 200, null = True)
	price 				= models.FloatField(null = True)
	category 			= models.CharField(max_length = 200, null = True, choices = CATEGORY)
	description 		= models.CharField(max_length = 200, null = True)
	date_created		= models.DateTimeField(auto_now_add = True, null = True)
	tag 				= models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

		
class Order(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Out of delivery','Out of delivery'),
		('Delivered','Delivered')
		)

	customer 			= models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
	product 			= models.ForeignKey(Product, null = True, on_delete=models.SET_NULL)
	date_created		= models.DateTimeField(auto_now_add = True, null = True)
	status 				= models.CharField(max_length = 100, choices = STATUS)
	note 				= models.CharField(max_length = 1000, null = True)

	def __str__(self):
		return str(self.product)
		
	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"


