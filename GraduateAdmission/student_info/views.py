from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, FileUploadForm
from .models import Profile
import datetime
from django.conf import settings
from .info2pdf import info2pdf


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
    if now.month >= settings.DEADLINE['month'] and now.day >= settings.DEADLINE['day'] and now.hour >= \
            settings.DEADLINE['hour']:
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
        update_fields = form.fields.keys()
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save(update_fields=update_fields)
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
    if request.method == 'POST' and 'personal_files' in request.FILES:
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


def download_form(request):
    from .models import interest_choices, exam_subject_choices
    from django.core.files.storage import FileSystemStorage

    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('/accounts/login')
    profile = Profile.objects.get(user=user)
    interest_dict = {x[0]: x[1] for x in interest_choices}
    interest_dict['None'] = ''
    subject_dict = {x[0]: x[1] for x in exam_subject_choices}
    info = {'name': str(profile.name), 'id': str(profile.student_id),  # basic information
            'university': str(profile.school), 'major': str(profile.major),
            'graduation_time': str(profile.graduate_year), 'email': str(profile.user.email),
            'mobile': str(profile.phone_number),
            'score_politics': str(profile.politics), 'score_english': str(profile.english),  # scores
            'score_third': str(profile.subject3_score), 'test_name_third': str(profile.subject3_name),
            'score_prof': str(profile.subject_major_score), 'test_name_prof': str(profile.subject_major_name),
            'score_total': str(profile.total_score),
            'orignial_target_major': str(profile.first_institute) + '-' + str(profile.first_major),  # targets
            'target_1': interest_dict[str(profile.interest1)],
            'target_2': interest_dict[str(profile.interest2)],
            'target_3': interest_dict[str(profile.interest3)],
            'target_4': interest_dict[str(profile.interest4)],
            'target_5': interest_dict[str(profile.interest5)],
            'chosen_test_name': subject_dict[profile.exam_subject]}
    info2pdf('/tmp/form-%s.pdf' % user, info=info)

    fs = FileSystemStorage("/tmp")
    with fs.open("form-%s.pdf" % user) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="form-%s.pdf"' % user
        return response
