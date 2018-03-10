from django.contrib import admin
from .models import Profile
from django.urls import path
from django.http import HttpResponse
from django.conf import settings

admin.site.disable_action('delete_selected')
admin.site.site_header = "清华大学工程物理系调剂信息管理系统"


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 1000
    exclude = ('user',)
    list_display = (
        'name', 'school', 'user_email',)
    list_display_links = ('name',)
    search_fields = ['name', 'school']

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = '邮箱'

    def get_urls(self):
        urlpatterns = super(ProfileAdmin, self).get_urls()
        urlpatterns.insert(0, path('download_profiles/', self.admin_site.admin_view(download_profile_view)))
        return urlpatterns


def download_profile_view(request):
    import pandas as pd
    import sqlite3
    from .models import Profile

    all_fields = Profile._meta.get_fields()
    download_fields_dict = {field.name: field.verbose_name for field in all_fields}
    download_fields_dict.pop('user')
    download_fields = list(download_fields_dict.keys())
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename={0}.xlsx".format("调剂表".encode('utf8').decode('ISO-8859-1'))
    db = settings.DATABASES['default']['NAME']
    con = sqlite3.connect(db)
    df = pd.read_sql_query("SELECT * from student_info_profile", con)
    df = df[download_fields]
    df.columns = [download_fields_dict[x] for x in df.columns]
    df.to_excel(response, index=False)
    return response
