from django.contrib import admin


# for registering this model to admin 
from .models import Profile

# Register your models here.
admin.site.register(Profile)