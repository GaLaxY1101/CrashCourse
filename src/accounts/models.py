from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Required class for custom user model
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not username:
			raise ValueError("Users must have an username")	
		user = self.model(
			email = self.normalize_email(email), # EMAIL@gmail.com ==> email@gmail.com
			username = username 
		)	
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_superuser(self,email,password,username):
		user = self.create_user(
			email = self.normalize_email(email), # EMAIL@gmail.com ==> email@gmail.com
			username = username,
			password = password
		)	
		user.is_superuser = True
		user.is_staff = True
		user.is_admin = True
		user.save(using=self.db)
		return user


#Custom user model
class Customer(AbstractBaseUser):
	username				= models.CharField(max_length = 50)
	email 					= models.EmailField(max_length = 250, unique = True)
	phone_number 			= models.CharField(max_length = 12)
	date_created			= models.DateTimeField(auto_now_add = True ,null = True)
	is_admin 				= models.BooleanField(default=False)
	is_staff 				= models.BooleanField(default=False)
	is_active 				= models.BooleanField(default=True)
	is_superuser 			= models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['username']
	
	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True	

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"




class Tag(models.Model):
	username 			= models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.username




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


