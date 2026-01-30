from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone

from .models import Article
from .forms import ArticleForm, CommentForm


# Create your views here.

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render(request,
                  'articles.html',
                  {'articles': Article.objects.all(),
                   'language': language,
                   'session_language': session_language})


def article(request, article_id=1):
    return render(request,
                  'article.html',
                  {'article': Article.objects.get(id=article_id)})


def language(request, language='en-gb'):
    response = HttpResponse(f"setting language to {language}")

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('article:all')
    else:
        form = ArticleForm()

    args = {'form': form}

    return render(request, 'create_article.html', args)


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return redirect('article:single', article_id=article_id)


def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()

            return redirect('article:single', article_id=article_id)

    else:
        f = CommentForm()

    args = {
        'article': a,
        'form': f,
    }

    return render(request, 'add_comment.html', args)

