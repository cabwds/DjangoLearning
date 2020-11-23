from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	# override the ModelForm default setting
	title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Title input"}))
	description=forms.CharField(required=False,
								 widget=forms.Textarea(
								 		attrs={
								 			"class":"new-class-name two",
								 			"id":"my-id-for-textarea",
								 			"rows":10,
								 			"cols":60,
								 			"placeholder":"Description input"
								 		})
								 )
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "Cab" in title:
			return forms.ValidationError("This is not a valid title")
		return title


class RawProductForm(forms.Form):
	title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Title input"}))
	description=forms.CharField(required=False,
								 widget=forms.Textarea(
								 		attrs={
								 			"class":"new-class-name two",
								 			"id":"my-id-for-textarea",
								 			"rows":10,
								 			"cols":60,
								 			"placeholder":"Description input"
								 		})
								 )
	price=forms.DecimalField(initial=199.99)