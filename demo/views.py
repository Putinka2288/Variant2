from django.contrib.auth.decorators import login_required
from django.core import validators
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from demo.forms import RegisterUserForm
from demo.models import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def validate_username(request):
    username = request.GET.get('username')
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


def validate_email(request):
    email = request.GET.get('email')
    try:
        validators.validate_email(email)
    except ValidationError as error:
        response = {
            'is_valid': False
        }
    else:
        response = {
            'is_valid': True,
            'is_taken': User.objects.filter(email__iexact=email).exists()
        }
    return JsonResponse(response)


def main(request):
    orders = Order.objects.all().order_by('-date')[:4]
    return render(request, 'demo/main.html', context={'orders': orders})


def register(request):
    return render(request, 'registration/register.html')


@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).all()
    return render(request, 'demo/orders.html', context={'orders': orders})


@login_required
def profail(request):
    return render(request, 'demo/profail.html')
