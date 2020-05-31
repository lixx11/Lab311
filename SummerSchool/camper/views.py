from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, FileUploadForm
from .models import Profile
from datetime import datetime
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


def download_form(request):
    from django.core.files.storage import FileSystemStorage
    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('/accounts/login')
    profile = Profile.objects.get(user=user)
    if profile.first_advisor is None or profile.first_advisor == '':
        first_advisor = '无'
    else:
        first_advisor = profile.first_advisor
    first_wish = f'{profile.first_institute}-{profile.first_degree}，专业：{profile.first_major}\n方向：{profile.first_interest}，导师：{first_advisor}'
    
    if profile.second_institute is None or profile.second_institute == '':
        second_wish = ''
    else:
        if profile.second_advisor is None or profile.second_advisor == '':
            second_advisor = '无'
        else:
            second_advisor = profile.second_advisor
        second_wish = f'{profile.second_institute}-{profile.second_degree}，专业：{profile.second_major}\n方向：{profile.second_interest}，导师：{second_advisor}'
    
    if profile.third_institute is None or profile.third_institute == '':
        third_wish = ''
    else:
        if profile.third_advisor is None or profile.third_advisor == '':
            third_advisor = '无'
        else:
            third_advisor = profile.third_advisor
        third_wish = f'{profile.third_institute}-{profile.third_degree}，专业：{profile.third_major}\n方向：{profile.third_interest}，导师：{third_advisor}'

    info = {
        'name': profile.name,
        'gender': profile.gender,
        'id_number': profile.id_number,
        'email': user.email,
        'phone_number': profile.phone_number,
        'school': profile.school,
        'department': profile.department,
        'major': profile.major,
        'major_number': str(profile.major_number),
        'admission_date': profile.admission_date,
        'graduation_date': profile.graduation_date,
        'average_score': profile.average_score,
        'major_rank': str(profile.major_rank),
        'english_level': profile.english_level,
        'first_wish': first_wish,
        'second_wish': second_wish,
        'third_wish': third_wish,
    }
    info2pdf('/tmp/form-%s.pdf' % user, info=info)

    fs = FileSystemStorage("/tmp")
    with fs.open("form-%s.pdf" % user) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="form-%s.pdf"' % user
        return response
