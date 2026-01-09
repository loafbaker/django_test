from django.urls import path, re_path

from . import views

app_name = 'article'

urlpatterns = [
    path('all/', views.articles),
    path('get/<int:article_id>/', views.article),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    path('create/', views.create),
    path('like/<int:article_id>/', views.like_article),
    path('add_comment/<int:article_id>/', views.add_comment),
]
