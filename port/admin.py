from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Skills)
#style="background: url( '{% static 'images/profile/profile-pic.png' %}');"
