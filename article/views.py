from django.shortcuts import render

from django.shortcuts import render_to_response
from article.models import Article, Comment
from django.http import HttpResponse
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone


# Create your views here.

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
   
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang'] 

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html', 
                             {'articles': Article.objects.all(),
                              'language': language,
                              'session_language': session_language })

def article(request, article_id=1):
    return render_to_response('article.html', 
                             {'article': Article.objects.get(id=article_id) })


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_article.html', args)

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)

def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()

            return HttpResponseRedirect('/articles/get/%s' % article_id)

    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))

    args['article'] = a
    args['form'] = f

    return render_to_response('add_comment.html', args)

