from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, FileUploadForm
from .models import Profile
from datetime import datetime
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

    now = datetime.now()
    deadline = datetime(int(settings.YEAR),
                        int(settings.DEADLINE['month']),
                        int(settings.DEADLINE['day']))
    if now > deadline:
        submission_over = True
    else:
        submission_over = False

    if request.method == 'POST':
        if submission_over:
            return HttpResponse('报名信息提交已截止！')
        profile = Profile.objects.get(user=user)
        if profile.is_confirmed == '是':
            return HttpResponse('申请表已确认，无法修改')

        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            update_fields = form.fields.keys()
            profile.save(update_fields=update_fields)
            profile = Profile.objects.get(user=user)
            profile_form = ProfileForm(instance=profile)
            file_upload_form = FileUploadForm(instance=profile)
            context = {
                'profile_form': profile_form,
                'file_upload_form': file_upload_form,
                'user': user
            }
            return render(request, 'camper/profile.html', context)
        else:
            return HttpResponse(form.errors)
    elif request.method == 'GET':
        profile = Profile.objects.get_or_create(user=user)[0]
        profile_form = ProfileForm(instance=profile)
        file_upload_form = FileUploadForm(instance=profile)
        context = {
            'profile_form': profile_form,
            'file_upload_form': file_upload_form,
            'user': user,
            'submission_over': submission_over,
            'release': settings.RELEASE,
            'profile': profile,
        }
        return render(request, 'camper/profile.html', context)


def submit_files(request):
    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('/accounts/login')

    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            file_fields = ['personal_statement', 'school_report', 'other_material']
            if 'personal_statement' in request.FILES:
                profile.personal_statement = request.FILES['personal_statement']
            else:
                file_fields.remove('personal_statement')
            if 'school_report' in request.FILES:
                profile.school_report = request.FILES['school_report']
            else:
                file_fields.remove('school_report')
            if 'other_material' in request.FILES:
                profile.other_material = request.FILES['other_material']
            else:
                file_fields.remove('other_material')
            profile.save(update_fields=file_fields)

            profile = Profile.objects.get(user=user)
            profile_form = ProfileForm(instance=profile)
            file_upload_form = FileUploadForm(instance=profile)
            context = {'profile_form': profile_form, 'file_upload_form': file_upload_form, 'user': user}
            return render(request, 'camper/profile.html', context)
    else:
        return redirect('/profile')
