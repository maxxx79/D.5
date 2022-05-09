from django import forms
# from django.forms import
from .models import Post, Author, Category
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from allauth.account.forms import LoginForm


class UserForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]

    def save(self, commit=True):
        user = super(UserForm, self).save()
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        print('Custom group works!')
        return user


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', max_length=128)
    text = forms.CharField(label='Текст', min_length=20, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
           'author',
           'post_category',
           'title',
           'text',
           'rating',
           ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту."
            )

        return cleaned_data


class CustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        print('Print login')
        print('self:', self)
        print(type(self))
        user = self.user
        print(user)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return super(CustomLoginForm, self).login(*args, **kwargs)


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

