from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	# override the ModelForm default setting
	title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder":"Title input"}))

	class Meta:
		model = Article
		fields = [
			'title',
			'content',
			'active'
		]

	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		#if not "Cab" in title:
		#	return forms.ValidationError("This is not a valid title")
		return title