from django.http import HttpResponse

def home(request):
    return HttpResponse("Ronilački klub - aplikacija radi ")