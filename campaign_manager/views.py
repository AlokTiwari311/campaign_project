from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Campaign Manager API!")
