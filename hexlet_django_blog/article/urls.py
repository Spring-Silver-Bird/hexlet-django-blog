from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleFormCreateView, ArticleListView, ArticleDetailView


urlpatterns = [
#    path('', ArticleListView.as_view(), name='article_list'),
    path("", IndexView.as_view(), name='article_list'),
    path("<int:id>/", ArticleDetailView.as_view(), name='article_detail'),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]