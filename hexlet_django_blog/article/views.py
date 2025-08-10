from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("article/index.html")

def index(request):
    return render(
        request,
        "index.html",
        context={
            'who': 'Article',
        }
    )