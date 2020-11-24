from django.urls import path
from .views import(
	article_list_view,
	article_detail_view,
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView,
)


app_name = 'blog'
urlpatterns = [
    #path('',article_list_view,name='article_list'),
    path('',ArticleListView.as_view(),name='article_list'),
    path('<int:id>/',ArticleDetailView.as_view(),name='article_detail'),
    path('create/',ArticleCreateView.as_view(),name='article_create'),
    path('<int:id>/update/',ArticleUpdateView.as_view(),name='article_update'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(),name='article_delete'),
]