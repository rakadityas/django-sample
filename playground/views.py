from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse("hello world")
    return render(request, 'sample.html', {"name": "Raka"})
