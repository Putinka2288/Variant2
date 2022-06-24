from django import forms
from django.core.validators import RegexValidator

from demo.models import User


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин',
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Логин занят'
                               })

    email = forms.EmailField(label='Почта',
                             error_messages={
                                 'invalid': 'Не правильный формат',
                                 'unique': 'Почта занята'
                             })

    password = forms.CharField(label='Пароль',
                               widget= forms.PasswordInput,
                               error_messages={
                                   'required': 'Обязательное поле'
                               })

    password2 = forms.CharField(label='Пароль(заного)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'Обязательное поле'
                                })

    name = forms.CharField(label='Имя',
                           error_messages={
                               'required': 'Обязательное поле'
                           })

    surname = forms.CharField(label='Фамилия',
                              error_messages={
                                  'required': 'Обязательное поле'
                              })

    patronymic = forms.CharField(label='Отество')

    rule = forms.BooleanField(label='Согласе с правилами',
                              initial=True,
                              required=True,
                              error_messages={
                                  'required': 'Обязательное поле'
                              })

    def save(self, commit=True):
        user = super().save(commit = True)
        user.set_password(self.cleaned_data.get('password2'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'name', 'surname', 'patronymic', 'rule')