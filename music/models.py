from django.db import models
# Create your models here.

CATEGORIES = (
	('all','All'),
	('sports','Sports'),
	('electric','Electrical Appliances'),
)

class Cart(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	checked_out = models.BooleanField(default=False)
	title = models.CharField(max_length = 50,default='')

	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(max_length = 200,default='')
	description = models.TextField()
	price = models.PositiveIntegerField()
	category = models.CharField(max_length = 50,choices = CATEGORIES,default = 'all')

	def __str__(self):
		return self.title

class Item(models.Model):
	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)

