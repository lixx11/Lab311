# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Info(models.Model):
    """Basic information of applicants"""
    # 姓名
    name = models.CharField(verbose_name='姓名', 
        max_length=128, blank=True)
    # 工作单位
    organization = models.CharField(verbose_name='工作单位', 
        max_length=128, blank=True)
    # 手机号
    phone_number = models.CharField(verbose_name='手机号', 
        max_length=128, blank=True)
    # 邮箱
    email = models.CharField(verbose_name='邮箱', 
        max_length=128, blank=True)
    # 人员类别
    BACHELOR, MASTER, DOCTOR, OTHER = 1, 2, 3, 0
    CATEGORY_CHOICES = (
            (BACHELOR, '本科'),
            (MASTER, '硕士'),
            (DOCTOR, '博士'),
            (OTHER, '其他'),
        )
    category = models.IntegerField(verbose_name='人员类别', 
        choices=CATEGORY_CHOICES, default=OTHER)
    # 审核结果
    UNCHECKED, PASSED, FAILED = 0, 1, 2
    CHECK_STATUS_CHOICES = (
            (UNCHECKED, '未审核'),
            (PASSED, '通过'),
            (FAILED, '未通过'),
        )
    check_status = models.IntegerField(verbose_name='审核结果',
        choices=CHECK_STATUS_CHOICES, default=UNCHECKED)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = '所有报名信息'
        