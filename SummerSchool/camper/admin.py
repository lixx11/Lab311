from django.contrib import admin
from .models import Profile
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings

admin.site.disable_action('delete_selected')
admin.site.site_header = "清华大学核学科夏令营管理后台"
site_readonly_fields = ['name', 'school', 'gender', 'age', 'phone_number', 'major_number', 'major_rank', 'class_number',
                        'class_rank', 'first_degree', 'second_degree', 'first_institute', 'second_institute',
                        'first_interest', 'second_interest', 'fund_applied', 'fund_application_text',
                        'personal_statement', 'school_report', 'other_material']


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 1000
    exclude = ('user',)
    list_display = (
        'name', 'school', 'user_email', 'major_rank2', 'class_rank2', 'dep_check_status', 'inet_check_status',
        'check_status', 'dep_retest_grade', 'inet_retest_grade')
    list_display_links = ('name',)
    readonly_fields = site_readonly_fields
    actions = ['send_email_action', ]
    search_fields = ['name', 'school', 'check_status', 'dep_retest_grade', 'inet_retest_grade']
    fieldsets = (
        ('基本信息', {
            'classes': ('extrapretty'),
            'fields': (('name', 'school', 'gender', 'age', 'phone_number'),)
        }),
        ('成绩', {
            'classes': ('extrapretty'),
            'fields': (('major_number', 'major_rank'), ('class_number', 'class_rank'),),
        }),
        ('志愿方向', {
            'classes': ('extrapretty',),
            'fields': (('first_degree', 'first_institute', 'first_interest'),
                       ('second_degree', 'second_institute', 'second_interest')),
        }),
        ('资助申请', {
            'classes': ('extrapretty',),
            'fields': ('fund_applied', 'fund_application_text', 'fund_status')
        }),
        ('文件', {
            'classes': ('extrapretty',),
            'fields': ('personal_statement', 'school_report', 'other_material')
        }),
        ('初试审核结果', {
            'classes': ('extrapretty',),
            'fields': ('dep_check_status', 'inet_check_status', 'check_status')
        }),
        ('复试结果', {
            'classes': ('extrapretty',),
            'fields': ('dep_retest_grade', 'inet_retest_grade')
        }),
    )

    def class_rank2(self, obj):
        return "%s / %s" % (obj.class_rank, obj.class_number)

    class_rank2.short_description = '班级排名'

    def major_rank2(self, obj):
        return "%s / %s" % (obj.major_rank, obj.major_number)

    major_rank2.short_description = '专业排名'

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
        urlpatterns.insert(0, path('show_statistics/', self.admin_site.admin_view(self.show_statistics_view)))
        urlpatterns.insert(0, path('download_profiles/', self.admin_site.admin_view(self.download_profile_view)))
        return urlpatterns

    def show_statistics_view(self, request):
        opts = self.model._meta
        context = {'opts': opts}
        return render(request, 'admin/statistics.html', context)

    def download_profile_view(self, request):
        return HttpResponse('下载表单')


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
        redirect_site = settings.WEBSITE + '/admin/camper/profile/'
        context = {"message": message, "redirect_site": redirect_site}
        return render(request, "admin/send_email_result.html", context)
    else:
        return redirect('/admin/camper/profile/')
