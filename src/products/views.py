from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_detail_view(request, my_id):
	#obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=my_id)
	

	#try:
	#	obj = Product.objects.get(id=my_id)
	#except Product.DoesNotExist:
	#	raise Http404

	context = {
		'obj':obj
	}
	return render(request,"product/detail.html",context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product,id=id)
	#POST request for deletion

	if request == "POST":
		obj.delete()
		
	context = {
		'obj':obj
	}
	return render(request,"product/product_delete.html",context)




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