from django.forms import ModelForm
from .models import Info


class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'organization', 'phone_number',
                  'email', 'category',
        ]