# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Info

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_per_page = 1000
    list_display = ('name',)

admin.site.register(Info, InfoAdmin)

