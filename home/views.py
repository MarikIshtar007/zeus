from django.shortcuts import render
from django.http import HttpResponse
from home.models import Product

# Create your views here.

def index(request):
	return HttpResponse("Hello")

def Home(request):
	# model = Product
	product_list = Product.objects.all()
	return render(request, "home/home.html", {
		"product_list": product_list
		})