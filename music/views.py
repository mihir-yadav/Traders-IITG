# from django.shortcuts import render/
from django.http import HttpResponseRedirect
# from django.template import loader 
from django.shortcuts import render, redirect
from . models import Product, Cart, Item

# Create your views here.
def index(request):
	all_products = Product.objects.all()
	# template = loader.get_template('music/index.html')
	context ={'all_products' : all_products,'n': Item.objects.count()}
	# return HttpResponse(template.render(context, request));
	return render (request , 'music/index.html',context)

def detail(request,product_id):
	return render(request,'music/detail.html',{'product':Product.objects.get(pk=product_id)})

def addInCart(request,product_id):
	if request.method == 'POST':
		cart = Cart.objects.get(pk=1)
		product = Product.objects.get(pk = product_id)

		try:
			item = Item.objects.get(cart = cart, product = product)
		except Item.DoesNotExist:
			item = Item()
			item.cart = cart
			item.product = product
			item.quantity = 1
			item.save()
		else:
			item.quantity += 1
			item.save()
		return redirect('index')

