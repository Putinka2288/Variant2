from django.contrib.auth import views as auth_view
from django.urls import path
from demo.views import *
from demo import views
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('validate_email', validate_email, name='validate_email'),
    path('validate_username', validate_username, name ='validate_username'),

    path('', main, name='main'),
    path('orders', orders, name='orders'),
    path('profail', profail, name='profail'),

]
