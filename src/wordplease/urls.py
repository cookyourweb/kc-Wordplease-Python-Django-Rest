"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from blogs.api import BlogsViewSet, BlogDetailViewSet, PostViewSet
from blogs.views import SignUpView, PostDetailView, home, CreatePostView, user_posts_list, blogs_list, search_categories
from users.api import UsersViewSet
from users.views import logout, LoginView

#  Router for the API
router = SimpleRouter()
router.register('users', UsersViewSet)
router.register('blogs/detail', BlogDetailViewSet)
router.register('blogs', BlogsViewSet),
router.register('post', PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', logout, name="logout_page"),
    path('signup/', SignUpView.as_view(), name="signup_page"),
    path('search/', search_categories),

    path('', home, name="home_page"),
    path('create-post/', CreatePostView.as_view(), name="create_post_page"),
    path('blogs/', blogs_list, name="blogs_list__page"),
    path('blogs/<nombre_usuario>', user_posts_list, name="posts_user_page"),
    path('posts/<int:pk>', PostDetailView.as_view(), name="post_detail_page"),

    # API de usuarios
    path('api/1.0/', include(router.urls))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
