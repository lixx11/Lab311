from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    # 基本信息
    user = models.OneToOneField(User, verbose_name='用户', on_delete=models.PROTECT, primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=128, blank=True, null=True)
    gender_choices = (('男', '男'), ('女', '女'))
    gender = models.CharField(verbose_name='性别', choices=gender_choices, max_length=128, blank=True, null=True)
    student_id = models.CharField(verbose_name='考生编号', max_length=128, blank=True, null=True)
    phone_number = models.CharField(verbose_name='手机号', max_length=128, blank=True, null=True)
    school = models.CharField(verbose_name='本科毕业学校', max_length=128, blank=True, null=True)
    major = models.CharField(verbose_name='本科专业', max_length=128, blank=True, null=True)
    graduate_year = models.IntegerField(verbose_name='本科毕业时间', blank=True, null=True)
    first_institute = models.CharField(verbose_name='原报考院系', max_length=128, blank=True, null=True)
    first_major = models.CharField(verbose_name='原报考专业', max_length=128, blank=True, null=True)
    yes_or_no_choices = (('否', '否'), ('是', '是'))
    exam_for_first_institute = models.CharField(verbose_name='是否参加原报考院系复试', choices=yes_or_no_choices,
                                                max_length=128, blank=True, null=True)

    # 成绩
    politics = models.IntegerField(verbose_name='政治', blank=True, null=True)
    english = models.IntegerField(verbose_name='英语', blank=True, null=True)
    subject3_name = models.CharField(verbose_name='科目三名称', max_length=128, blank=True, null=True)
    subject3_score = models.IntegerField(verbose_name='科目三成绩', blank=True, null=True)
    subject_major_name = models.CharField(verbose_name='专业课名称', max_length=128, blank=True, null=True)
    subject_major_score = models.IntegerField(verbose_name='专业课成绩', blank=True, null=True)
    total_score = models.IntegerField(verbose_name='总分', blank=True, null=True)

    # 志愿
    interest_choices = (
        (
            '核能',
            '核能方向 - 核能与核技术工程（085226）- 清华本部'
        ),
        (
            '核燃料',
            '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'
        ),
        (
            '核技术',
            '核技术方向 - 核能与核技术工程（085226）- 清华本部'
        ),
        (
            '公共安全',
            '公共安全 - 安全工程（085224） - 深圳研究生院',
        ),
        (
            '核能安全',
            '核能安全 - 安全工程（085224） - 深圳研究生院',
        ),
    )
    interest1 = models.CharField(verbose_name='第一志愿', choices=interest_choices, max_length=8, blank=True, null=True)
    interest2 = models.CharField(verbose_name='第二志愿', choices=interest_choices, max_length=8, blank=True, null=True)
    interest3 = models.CharField(verbose_name='第三志愿', choices=interest_choices, max_length=8, blank=True, null=True)
    interest4 = models.CharField(verbose_name='第四志愿', choices=interest_choices, max_length=8, blank=True, null=True)
    interest5 = models.CharField(verbose_name='第五志愿', choices=interest_choices, max_length=8, blank=True, null=True)

    exam_subject_choices = (
        ('安全系统', '安全系统工程'),
        ('热工', '热工基础'),
        ('力学', '力学基础'),
        ('核物理', '核物理'),
        ('辐射防护', '辐射防护'),
        ('信号与系统', '信号与系统'),
    )

    exam_subject = models.CharField(verbose_name='考试科目', choices=exam_subject_choices, max_length=128, blank=True,
                                    null=True)

    # 文件
    personal_files = models.FileField(verbose_name='所有材料', upload_to='uploads', blank=True, null=True)

    # 确认提交
    is_confirmed = models.CharField(verbose_name='确认提交', choices=yes_or_no_choices, max_length=128, default='否',
                                    blank=True)

    class Meta:
        verbose_name = '调剂信息'
        verbose_name_plural = '所有调剂信息'