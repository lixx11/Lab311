from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def index(request):
    return redirect('accounts/login')


def submit_profile(request):
    # 获取用户信息
    try:
        username = request.user.username
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return redirect('accounts/login')

    if request.method == 'POST':
        profile = Profile.objects.get(user=user)
        if profile.is_confirmed == 1:  # 如果确认，不再修改
            return HttpResponse('申请表已确认，无法修改')

        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            update_fields = list(form.fields.keys())
            if 'confirm' in request.POST:
                profile.is_confirmed = 1
            else:
                profile.is_confirmed = 0
            update_fields.append('is_confirmed')
            try:
                profile.save(update_fields=update_fields)
            except:
                profile.save()
            context_dict = {'form': form}
            return render(request, 'camper/profile.html', context_dict)
        else:
            return HttpResponse(form.errors)
    elif request.method == 'GET':
        profile = Profile.objects.get_or_create(user=user)[0]
        profile_form = ProfileForm(instance=profile)
        context_dict = {'form': profile_form}
        return render(request, 'camper/profile.html', context_dict)