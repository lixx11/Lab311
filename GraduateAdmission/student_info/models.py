from django.db import models
from django.contrib.auth.models import User


# 志愿
interest_choices = (
    (
        '能源动力-核能与核技术工程（清华本部）- 核能方向',
        '能源动力-核能与核技术工程（清华本部）- 核能方向'
    ),
    (
        '能源动力-核能与核技术工程（清华本部）-核技术方向',
        '能源动力-核能与核技术工程（清华本部）-核技术方向'
    ),
    (
        '能源动力-核能与核技术工程（清华本部）-临床医学交叉人才培养项目',
        '能源动力-核能与核技术工程（清华本部）-临床医学交叉人才培养项目'
    ),
    (
        '安全科学与技术',
        '安全科学与技术',
    ),
    (
        '资源与环境-安全工程（深研院）-公共安全方向',
        '资源与环境-安全工程（深研院）-公共安全方向',
    ),
    (
        '资源与环境-安全工程（深研院）-核能方向',
        '资源与环境-安全工程（深研院）-核能方向',
    )
)

exam_subject_choices = (
    ('安全系统工程', '安全系统工程'),
    ('热工基础', '热工基础'),
    ('核燃料循环与材料基础', '核燃料循环与材料基础'),
    ('核物理', '核物理'),
    ('辐射防护', '辐射防护'),
    ('信号与系统', '信号与系统'),
)

# Create your models here.


class Profile(models.Model):
    # 基本信息
    user = models.OneToOneField(
        User, verbose_name='用户', on_delete=models.PROTECT, primary_key=True)
    name = models.CharField(
        verbose_name='姓名', max_length=128, blank=True, null=True)
    gender_choices = (('男', '男'), ('女', '女'))
    gender = models.CharField(
        verbose_name='性别', choices=gender_choices, max_length=128, blank=True, null=True)
    student_id = models.CharField(
        verbose_name='考生编号', max_length=128, blank=True, null=True)
    phone_number = models.CharField(
        verbose_name='手机号', max_length=128, blank=True, null=True)
    school = models.CharField(verbose_name='本科毕业学校',
                              max_length=128, blank=True, null=True)
    major = models.CharField(
        verbose_name='本科专业', max_length=128, blank=True, null=True)
    graduate_year = models.IntegerField(
        verbose_name='本科毕业时间', blank=True, null=True)
    first_institute = models.CharField(
        verbose_name='原报考院系', max_length=128, blank=True, null=True)
    first_major = models.CharField(
        verbose_name='原报考专业', max_length=128, blank=True, null=True)
    exam_or_not_choices = (('不参加', '不参加'), ('参加', '参加'))
    exam_for_first_institute = models.CharField(verbose_name='是否参加原报考院系复试', choices=exam_or_not_choices,
                                                max_length=128, blank=True, null=True)

    # 成绩
    politics = models.IntegerField(verbose_name='政治', blank=True, null=True)
    english = models.IntegerField(verbose_name='英语', blank=True, null=True)
    subject3_name = models.CharField(
        verbose_name='科目三名称', max_length=128, blank=True, null=True)
    subject3_score = models.IntegerField(
        verbose_name='科目三成绩', blank=True, null=True)
    subject_major_name = models.CharField(
        verbose_name='专业课名称', max_length=128, blank=True, null=True)
    subject_major_score = models.IntegerField(
        verbose_name='专业课成绩', blank=True, null=True)
    total_score = models.IntegerField(verbose_name='总分', blank=True, null=True)

    interest1 = models.CharField(
        verbose_name='第一志愿', choices=interest_choices, max_length=128, blank=True, null=True)
    interest2 = models.CharField(
        verbose_name='第二志愿', choices=interest_choices, max_length=128, blank=True, null=True)
    interest3 = models.CharField(
        verbose_name='第三志愿', choices=interest_choices, max_length=128, blank=True, null=True)
    interest4 = models.CharField(
        verbose_name='第四志愿', choices=interest_choices, max_length=128, blank=True, null=True)
    interest5 = models.CharField(
        verbose_name='第五志愿', choices=interest_choices, max_length=128, blank=True, null=True)
    interest6 = models.CharField(
        verbose_name='第六志愿', choices=interest_choices, max_length=128, blank=True, null=True)

    exam_subject = models.CharField(verbose_name='考试科目', choices=exam_subject_choices, max_length=128, blank=True,
                                    null=True)

    # 文件
    personal_files = models.FileField(
        verbose_name='所有材料', upload_to='uploads', blank=True, null=True)

    # 确认提交
    yes_or_no_choices = (('否', '否'), ('是', '是'))
    is_confirmed = models.CharField(verbose_name='确认提交', choices=yes_or_no_choices, max_length=128, default='否',
                                    blank=True)

    # 审核结果
    check_choices = (('未审核', '未审核'), ('通过', '通过'), ('不通过', '不通过'))
    check_status = models.CharField(verbose_name='审核结果', choices=check_choices, max_length=128, default='未审核',
                                    blank=True, null=True)

    class Meta:
        verbose_name = '调剂信息'
        verbose_name_plural = '所有调剂信息'
