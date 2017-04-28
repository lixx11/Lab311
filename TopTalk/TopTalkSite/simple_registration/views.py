# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm

# Create your views here.
def index(request):
    info_form = InfoForm()
    context = {'form': info_form}
    return render(request, 'index.html', context)