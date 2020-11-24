from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.urls import reverse
# Create your views here.

def article_list_view(request):
	queryset = Article.objects.all() #list of objects
	context = {
		'obj_list':queryset
	}
	return render(request,"blog/article_list.html",context)


def article_detail_view(request,id):
	obj = get_object_or_404(Article, id=id)
	context = {
		'obj':obj
	}
	return render(request,"blog/article_detail.html",context)



from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

# used class based view
class ArticleListView(ListView):
	template_name = 'blog/article_list.html'
	queryset = Article.objects.all()	# <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
	template_name = 'blog/article_detail.html'
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	# success_url = "/"

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_update.html'
	form_class = ArticleForm
	queryset = Article.objects.all()
	# success_url = "/"

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'blog/article_delete.html'
	#success_url = 'blog/'
	# without specifying the success url, it will make the deletion action fail
	def get_success_url(self):
		return reverse('blog:article_list')

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)