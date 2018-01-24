from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView

from blogs.forms import SignUpForm, PostForm, BlogForm

from blogs.models import Post, Category, Blog


def home(request):
    now = datetime.now()
    all_post = Post.objects.filter(publish_date__lte=now).order_by("-publish_date")
    context = {'posts': all_post}
    return render(request, "home.html", context)


def user_posts_list(request, nombre_usuario):
    now = datetime.now()
    #  Categorias para el filtro
    categories = Category.objects.all().order_by("name")
    posts_list = Post.objects.filter(user__username=nombre_usuario, publish_date__lte=now).order_by("-publish_date")
    # Información para la cabecera del blog
    try:
        blog_info = Blog.objects.get(user__username=nombre_usuario)
    except:
        return render(request, "404.html")
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts, 'blog': blog_info, 'categories': categories, 'owner': nombre_usuario}
    return render(request, "my_blog.html", context)


def blogs_list(request):
    all_blogs = Blog.objects.filter().order_by("blog_name")
    return render(request, "blogs_list.html", {"blogs": all_blogs})


def search_categories(request):
    now = datetime.now()
    #  Categorias para el filtro
    categories = Category.objects.all().order_by("name")
    username = request.GET.get('owner')
    idcat = request.POST.get('categoria')
    if idcat == '0':
        posts_list = Post.objects.filter(user__username=username, publish_date__lte=now).order_by("-publish_date")
    else:
        posts_list = Post.objects.filter(categories__in=[idcat], user__username=username,
                                         publish_date__lte=now).order_by("-publish_date")
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts, 'owner': username, 'categories': categories}
    return render(request, "my_blog.html", context)


class SignUpView(View):

    def get(self, request):
        formUser = SignUpForm()
        formBlog = BlogForm()
        return render(request, "signup.html", {"formUser": formUser, "formBlog": formBlog})

    def post(self, request):
        user_form = SignUpForm(request.POST)
        blog_form = BlogForm(request.POST)
        if user_form.is_valid() and blog_form.is_valid():
            # User save from form
            user = user_form.save()
            user.blog.blog_name = blog_form.instance.blog_name
            user.blog.blog_description = blog_form.instance.blog_description
            user.save()
            #  User autenctication
            login(request, user)
            return redirect("home_page")
        return render(request, "signup.html", {"formUser": user_form, "formBlog": blog_form})


class CreatePostView(LoginRequiredMixin, View):

    login_url = "/login"

    def get(self, request):
        form = PostForm()
        return render(request, "create_post_form.html", {"form": form})

    def post(self, request):
        post = Post()
        post.user = request.user  #select user autenticated
        form = PostForm(request.POST,  request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        return render(request, "create_post_form.html", {"form": form})


class PostDetailView(DetailView):

    model = Post
    template_name = 'post_detail.html'

    def get_queryset(self):
        query = super(PostDetailView, self).get_queryset()
        now = datetime.now()
        return query.filter(publish_date__lte=now)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return render(request,"404.html")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)