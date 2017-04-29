# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Info
from django.shortcuts import render
from django.conf.urls import url
from django.core.mail import send_mail, EmailMessage, get_connection
from django.core.mail.backends.smtp import EmailBackend
from django.contrib.sites.shortcuts import get_current_site


# Register your models here.
# 禁止管理员在索引页进行删除操作
admin.site.disable_action('delete_selected')
# 设置管理系统名称
admin.site.site_header = "海外学者讲学报名管理系统"


class InfoAdmin(admin.ModelAdmin):
    # 每页最多显示1000项
    list_per_page = 1000
    # 索引页显示字段
    list_display = ('name', 'organization', 'phone_number',
                    'email', 'category', 'check_status')
    # 管理员只读字段
    readonly_fields = ('name', 'organization', 'phone_number',
                       'email', 'category')
    # 可搜索字段
    search_fields = ['name', 'organization', 'category']
    # 自定义管理员功能
    actions = ['batch_pass', 
               'batch_fail',
               'send_email_action']

    # 索引页批处理通过
    def batch_pass(self, request, queryset):
        queryset.update(check_status=Info.PASSED)
    batch_pass.short_description = '审核通过'

    # 索引页批处理未通过
    def batch_fail(self, request, queryset):
        queryset.update(check_status=Info.FAILED)
    batch_fail.short_description = '审核未通过'

    # 发送邮件
    def send_email_action(self, request, queryset):
        recipient_list = []
        count = 0
        for obj in queryset:
            email = obj.email
            name = obj.name
            name_tag = "email_tag" + str(count)
            recipient_list.append([name, email, name_tag])
            count += 1
        context_dict = {"recipient_list": recipient_list}
        response = render(request, "admin/send_email.html", context_dict)
        return response
    send_email_action.short_description = '发送邮件'

    def send_email_view(self, request):
        if request.method == 'POST':
            # parse POST 
            from_email = request.POST['email']
            passwd = request.POST['passwd']
            email_content = request.POST['email_content_text']
            subject = request.POST['subject']

            # 获取收件人
            recipient_list = []
            post_keys = request.POST.keys()
            for i in range(len(post_keys)):
                post_field = post_keys[i]
                if post_field[0:9] == "email_tag":
                    recipient_list.append(request.POST[post_field])

            # 发送邮件
            username, host = from_email.split('@')
            try:
                backend = EmailBackend(
                    host=host,
                    username=username,
                    password=passwd,
                    from_email=from_email,
                    )
                backend.open()
                num_sent = EmailMessage(
                        subject=subject,
                        body=email_content,
                        to=recipient_list,
                        connection=backend,
                        from_email=from_email,
                    ).send()
                backend.close()
            except:
                username = from_email
                backend = EmailBackend(
                    host=host,
                    username=username,
                    password=passwd,
                    )
                backend.open()
                num_sent = EmailMessage(
                        subject=subject,
                        body=email_content,
                        from_email=from_email,
                        to=recipient_list,
                        connection=backend,
                    ).send()
                backend.close()

            # render response
            result = num_sent > 0
            root_url = str(get_current_site(request))
            path_split = request.path.split('/')
            redirect_site = 'http://%s/admin/%s/%s' % (
                root_url, path_split[2], path_split[3])
            context_dict = {"result": result, 
                "redirect_site": redirect_site}
            return render(request, 
                "admin/send_email_result.html", context_dict)

    # 插入send_email view
    def get_urls(self):
        urlpatterns = super(InfoAdmin, self).get_urls()
        urlpatterns.insert(0, url(r'^send_email/', 
            self.admin_site.admin_view(self.send_email_view)))
        return urlpatterns


# 在管理系统注册model和对应的admin
admin.site.register(Info, InfoAdmin)

