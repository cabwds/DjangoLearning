from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_detail_view(request, id):
	#obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=id)
	

	#try:
	#	obj = Product.objects.get(id=my_id)
	#except Product.DoesNotExist:
	#	raise Http404

	context = {
		'obj':obj
	}
	return render(request,"product/product_detail.html",context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product,id=id)
	#POST request for deletion

	if request.method == "POST":
		#confirming delete
		obj.delete()
		#redirect after deletion to be home list page
		return redirect('../../../products/') 
	context = {
		'obj':obj
	}
	return render(request,"product/product_delete.html",context)

def product_list_view(request):
	queryset = Product.objects.all() #list of objects
	context = {
		'obj_list':queryset
	}
	return render(request,"product/product_list.html",context)


def product_update_view(request,id=id):
	obj = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return redirect('../')
		
	context = {
		'form':form
	}
	return render(request,"product/product_update.html",context)


### example of raw form ###
#def product_create_view(request):
#	my_form = RawProductForm()
#	if request.method == "POST":
#		my_form = RawProductForm(request.POST)
#		if my_form.is_valid():
#			# now the data is good
#			print(my_form.cleaned_data)
#			# use ** to turn dict type arguments
#			Product.objects.create(**my_form.cleaned_data)
#		else:
#			print(my_form.errors)
#	
#	context={
#		'form':my_form
#	}
#	return render(request,"product/product_create.html",context)

### example of form for creating object ###
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form':form
	}
	return render(request,"product/product_create.html",context)


### example of raw HTML ###
#def product_create_view(request):
#	#print(request.GET)
#	#print(request.POST)
#	if request.method == "POST":
#		new_title=request.POST.get('title')
#		print(new_title)
#		#Product.objects.create(title=new_title)
#	context={}
#	return render(request,"product/product_create.html",context)