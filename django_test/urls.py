from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),

    url(r'^hello/', 'article.views.hello'),
    url(r'^hello_template/', 'article.views.hello_template'),
    url(r'^hello_simple_template/', 'article.views.hello_simple_template'),
    url(r'^hello_class_view/', HelloTemplate.as_view()),
)
