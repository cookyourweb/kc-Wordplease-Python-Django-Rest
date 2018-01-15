from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView



from articles.forms import BlogForm
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

def article_detail(request, pk):
    possible_articles = Article.objects.filter(pk=pk).select_related("category")
    if len(possible_articles) == 0:
        return render(request, "404.html", status=404)
    else:
        article = possible_articles[0]
        context = {'article': Article}
        return render(request, "article_detail.html", context)

class CreateBlogsView(LoginRequiredMixin, View):

        def get(self, request):
            form = BlogForm()

        def post(self, request):
            blog = Article()
            blog.user = request.user
            form = BlogForm(request.POST, instance=blog)
            if form.is_valid():
                blog = form.save()
                form = BlogForm()
                url = reverse("articlegit _detail_page", args=[blog.pk])
                message = "Blog created successfully! "
                message += '<a href="{0}">View</a>'.format(url)
                messages.success(request, message)

            return render(request, "blog_form.html", {'form': form})