from django.contrib import admin

# Register your models here.
from demo.models import *

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Category)