from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, DateTimeInput, SelectMultiple, TextInput

from blogs.models import Post, Blog


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        del self.fields['password2']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_name', 'blog_description')


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ['user']
        widgets = {"title": TextInput(attrs={'rows': 3, 'class': 'form-control'}),
                   "intro": Textarea(attrs={'rows': 3, 'class': 'form-control'}),
                   "body": Textarea(attrs={'rows': 10, 'class': 'form-control'}),
                   'publish_date': DateTimeInput(attrs={'class': 'datepicker'}),
                   'categories': SelectMultiple(attrs={'class': 'form-control'})
                   }
