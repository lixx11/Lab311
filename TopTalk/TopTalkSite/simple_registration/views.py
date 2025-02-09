# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Info
from .forms import InfoForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = InfoForm()
        context = {'form': form}
        # weihe edited: wrong template path. 04/29
        return render(request, 'simple_registration/index.html', context)
    else:
        form = InfoForm(request.POST)
        if form.is_valid():
            info = form.save()
            return HttpResponse('成功提交表单')
        else:
            return HttpResponse('表单错误！')