from django.urls import path
from .views import(
	article_list_view,
	article_detail_view
)


app_name = 'blog'
urlpatterns = [
    path('',article_list_view,name='article_list'),
    path('<int:id>/',article_detail_view,name='article_detail'),
]