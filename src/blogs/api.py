from datetime import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import BlogPermissions, BlogDetailPermissions, PostPermissions
from blogs.serializers import BlogSerializer, BlogDetailSerializer, PostCreateSerializer, PostSerializer


class BlogsViewSet(ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__username']
    order_fields = ['blog_name']


class BlogDetailViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [BlogDetailPermissions]

    def retrieve(self, request, pk=None):
        now = datetime.now()
        if request.user.is_superuser or (request.user.is_authenticated and str(request.user.id) == pk):
            posts_list = Post.objects.filter(user=pk).order_by('-publish_date')
        else:
            posts_list = Post.objects.filter(user=pk, publish_date__lte=now).order_by('-publish_date')
        #  filtro por aproximación en los campos title y body
        search_param = self.request.query_params.get('search', None)
        if search_param is not None:
            posts_list = posts_list.filter(Q(title__contains=search_param) | Q(body__contains=search_param))
        #  ordenar por campo
        order_field = self.request.query_params.get('ordering', None)
        if order_field is not None:
            posts_list = posts_list.order_by(order_field)
        serializer = BlogDetailSerializer(posts_list, many=True)
        return Response(serializer.data)

    def create(self, request):
        post = Post()
        post.user = request.user
        serializer = PostCreateSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermissions]

    def update(self, request, pk=None):
        post = self.get_object()
        serializer = PostCreateSerializer(data=request.data, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
