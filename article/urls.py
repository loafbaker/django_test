from django.urls import path, re_path

from . import views

app_name = 'article'

urlpatterns = [
    path('all/', views.articles, name='all'),
    path('get/<int:article_id>/', views.article, name='single'),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language, name='language'),
    path('create/', views.create, name='create'),
    path('like/<int:article_id>/', views.like_article, name='like_article'),
    path('add_comment/<int:article_id>/', views.add_comment, name='add_comment'),
]
