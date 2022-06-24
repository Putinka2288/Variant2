from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Роль', choices=(('user', "Пользователь"),
                                                                          ('admin', "Администратор")), default='user')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [('new', 'Новая'), ('repairing', 'Ремонтируется'), ('renovated', 'Отремонтировано')]
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)
    address = models.CharField(max_length=254, verbose_name='Адресс помещения', blank=False)
    description = models.TextField(verbose_name='Описание заявки', blank=False)
    max_price = models.DecimalField(verbose_name='Максимальная цена', max_digits=10, decimal_places=2, default=0.00,
                                    blank=True)
    photo_file_after = models.ImageField(max_length=254, null=True, blank=True, upload_to=get_name_file,
                                         validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg',
                                                                                                'png', 'bmp'])])
    photo_file_before = models.ImageField(max_length=254, null=True, blank=True, upload_to=get_name_file,
                                          validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg',
                                                                                                 'png', 'bmp'])])
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    price_done = models.DecimalField(verbose_name='Согласованная цена', max_digits=10, decimal_places=2, default=0.00,
                                     null=True, blank=True)
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.user.name

    def status_verbose(self):
        return dict(self.STATUS_CHOICES)[self.status]


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Категория', blank=False)

    def __str__(self):
        return self.name