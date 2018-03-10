from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['personal_files', 'user']


class FileUploadForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['personal_files', ]
