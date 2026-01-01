from django.urls import path, re_path

from . import views

app_name = 'article'

urlpatterns = [
    path('all/', views.articles),
    re_path(r'^get/(?P<article_id>\d+)/$', views.article),
    re_path(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    path('create/', views.create),
    re_path(r'^like/(?P<article_id>\d+)/$', views.like_article),
    re_path(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment),
]
