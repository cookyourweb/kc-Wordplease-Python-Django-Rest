from django.forms import ModelForm

from articles.models import Article


class BlogForm(ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ["user"]
