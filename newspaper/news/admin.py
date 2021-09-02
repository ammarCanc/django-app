"""
Configurations for News app Admin
"""
from django.contrib import admin
from .models import *


admin.site.register(Article)
admin.site.register(Blog)
admin.site.register(User)
admin.site.register(NewsBulletin)
