from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, FileUploadForm
from .models import Profile
import datetime
from django.conf import settings


# Create your views here.
def index(request):
    return redirect('/accounts/login')


def submit_profile(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('/accounts/login')

    now = datetime.datetime.now()
    if now.month >= settings.DEADLINE['month'] and now.day >= settings.DEADLINE['day']:
        submission_over = True
    else:
        submission_over = False

    if request.method == 'POST':
        if submission_over:
            return HttpResponse('调剂信息提交已截止！')
        profile = Profile.objects.get(user=user)
        if profile.is_confirmed == '是':
            return HttpResponse('调剂信息已确认，无法修改')

        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            profile = Profile.objects.get(user=user)
            profile_form = ProfileForm(instance=profile)
            file_upload_form = FileUploadForm(instance=profile)
            context = {'profile_form': profile_form, 'file_upload_form': file_upload_form, 'user': user}
            return render(request, 'student_info/profile.html', context)
        else:
            return HttpResponse(form.errors)
    elif request.method == 'GET':
        profile = Profile.objects.get_or_create(user=user)[0]
        profile_form = ProfileForm(instance=profile)
        file_upload_form = FileUploadForm(instance=profile)
        context = {'profile_form': profile_form, 'file_upload_form': file_upload_form, 'user': user,
                   'submission_over': submission_over}
        return render(request, 'student_info/profile.html', context)


def submit_files(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('/accounts/login')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save(update_fields=['personal_files', ])

            profile = Profile.objects.get(user=user)
            profile_form = ProfileForm(instance=profile)
            file_upload_form = FileUploadForm(instance=profile)
            context = {'profile_form': profile_form, 'file_upload_form': file_upload_form, 'user': user}
            return render(request, 'student_info/profile.html', context)
        else:
            return HttpResponse(form.errors)
    else:
        return redirect('/profile')
