from django.shortcuts import render

from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse


# Create your views here.

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
   
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang'] 

    return render_to_response('articles.html', 
                             {'articles': Article.objects.all(),
                              'language': language })

def article(request, article_id=1):
    return render_to_response('article.html', 
                             {'article': Article.objects.get(id=article_id) })


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    return response
