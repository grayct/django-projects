# Create your views here.
from django.http import HttpResponse
from django.template import Context, RequestContext, loader

def home(request):
    home_page = loader.get_template('index.html')
    return HttpResponse(home_page.render(RequestContext(request)))