from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


# Create your views here.



def hello(request):
    name = "Jianming Chen"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Jianming Chen"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def hello_simple_template(request):
    name = "Jianming Chen"
    return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_contet_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Jianming Chen'
        return context

