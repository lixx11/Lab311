from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'personal_statement', 'school_report', 'other_material', 'check_status', 'fund_status',
                   'dep_check_status', 'inet_check_status', 'dep_retest_grade', 'inet_retest_grade']


class FileUploadForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['personal_statement', 'school_report', 'other_material']
