from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from articles.models import Article


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello keepcoders!")
    else:
        return HttpResponse("Hello " + name)


def home(request):
    last_articles = Article.objects.all().order_by("-release_date")[:3]
    context = {'articles': last_articles[:5]}
    return render(request, "home.html", context)