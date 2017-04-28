# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Info(models.Model):
    """Basic information of applicants"""
    name = models.CharField(verbose_name='姓名', 
        max_length=128, blank=True)
    organization = models.CharField(verbose_name='工作单位', 
        max_length=128, blank=True)
    phone_number = models.CharField(verbose_name='手机号', 
        max_length=128, blank=True)
    email = models.CharField(verbose_name='邮箱', 
        max_length=128, blank=True)
    category = models.CharField(verbose_name='人员类别', 
        choices=(('1', '本科'), ('2', '硕士'), ('3', '博士'), ('4', '其他')),
        max_length=128, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '所有用户信息'
        