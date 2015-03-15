# coding: utf8
from .models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


# Допиливаем форму добавления пользователя. В Meta.model указываем нашу модель.
# Добавляем обязательное поле email и фиксим один метод, который почему-то явно
# стандартную модель, а не рекомендуемый get_user_model.
class AdminUserAddForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


# Допиливаем форму редактирования пользователя. В Meta.model указываем нашу модель.
class AdminUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = "__all__"


class LoginForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    is_remember = forms.BooleanField(required=False)

    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #     login = cleaned_data.get("login")
    #
    #     try:
    #         user = User.objects.get(phone=login)
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("Не правельный логин или пароль")
    #
    #     return cleaned_data


class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']