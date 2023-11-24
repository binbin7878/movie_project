from django.contrib import admin
from .models import Profile
from .models import Movieinfo
from .models import MovieReserve


# Register your models here.

admin.site.register(Profile)
admin.site.register(Movieinfo)
admin.site.register(MovieReserve)
