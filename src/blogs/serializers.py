from rest_framework import serializers

from blogs.models import Blog, Post, Category


class BlogSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')
    url = serializers.SerializerMethodField('create_url')

    def create_url(self, blog):
        request = self.context.get('request')
        return request.build_absolute_uri('detail/'+str(blog.user.id)+'/')

    class Meta:
        model = Blog
        fields = ['id', 'blog_name', 'blog_description', 'owner', 'url']


class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'intro', 'image', 'publish_date']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description')


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'intro', 'publish_date', 'body']


class PostSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
