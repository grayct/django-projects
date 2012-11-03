from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to grayct learning django.")
