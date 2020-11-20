from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
	print(request)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code

	my_context = {
		"my_text":"text1",
		"my_number": 1234,
		"my_list":{
			"token":"xxxxyyy",
			"accesstoken":"vdshei",
			"expiredin":329885
		}
	}
	return render(request,"home.html",my_context)