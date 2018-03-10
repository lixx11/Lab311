from django.contrib import admin
from .models import Profile
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend

admin.site.disable_action('delete_selected')
admin.site.site_header = "清华大学工程物理系调剂信息管理系统"
_all_fields = Profile._meta.get_fields()
all_fields = [field.name for field in _all_fields]


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 1000
    exclude = ('user',)
    list_display = (
        'name', 'school', 'user_email', 'check_status')
    list_display_links = ('name',)
    search_fields = ['name', 'school']
    readonly_fields = all_fields.copy()
    readonly_fields.remove('check_status')
    actions = ['send_email_action', ]

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = '邮箱'

    def send_email_action(self, request, queryset):
        opts = self.model._meta
        recipients = []
        count = 0
        for obj in queryset:
            email = obj.user.email
            name = obj.name
            email_tag = "email_tag" + str(count)
            recipients.append([name, email, email_tag])
            count += 1
        context = {'opts': opts, 'recipients': recipients}
        return render(request, 'admin/send_email.html', context)

    send_email_action.short_description = '发送邮件'

    def get_urls(self):
        urlpatterns = super(ProfileAdmin, self).get_urls()
        urlpatterns.insert(0, path('send_email/', self.admin_site.admin_view(send_email_view)))
        urlpatterns.insert(0, path('download_profiles/', self.admin_site.admin_view(download_profile_view)))
        return urlpatterns


def download_profile_view(request):
    import pandas as pd
    import sqlite3

    download_fields_dict = {field.name: field.verbose_name for field in _all_fields}
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


def send_email_view(request):
    if request.method == 'POST':
        email_content = request.POST['email_content_text']
        subject = request.POST['subject']
        recipients = []
        post_keys = list(request.POST.keys())
        for i in range(len(post_keys)):
            post_field = post_keys[i]
            if post_field[0:9] == "email_tag":
                recipients.append(request.POST[post_field])
        backend = EmailBackend(
            host=settings.OFFICIAL_EMAIL_HOST,
            username=settings.OFFICIAL_EMAIL_HOST_USER,
            password=settings.OFFICIAL_EMAIL_HOST_PASSWORD)
        backend.open()
        num_sent = EmailMessage(
            subject=subject,
            body=email_content,
            from_email=settings.OFFICIAL_FROM_EMAIL,
            to=recipients,
            connection=backend,
        ).send()
        backend.close()

        message = "%d mail(s) sent to %d recipient(s)" % (num_sent, len(recipients))
        redirect_site = 'http://' + settings.WEBSITE + '/admin/student_info/profile/'
        context = {"message": message, "redirect_site": redirect_site}
        return render(request, "admin/send_email_result.html", context)
    else:
        return redirect('/admin/student_info/profile/')