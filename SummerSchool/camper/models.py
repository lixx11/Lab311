from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    # 基本信息
    user = models.OneToOneField(User, verbose_name='用户', on_delete=models.PROTECT, primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=128, blank=True, null=True)
    school = models.CharField(verbose_name='学校', max_length=128, blank=True, null=True)
    gender_choices = (('男', '男'), ('女', '女'))
    gender = models.CharField(verbose_name='性别', choices=gender_choices, max_length=128, blank=True, null=True)
    age = models.IntegerField(verbose_name='年龄', blank=True, null=True)
    major = models.CharField(verbose_name='专业', max_length=128, blank=True, null=True)
    id_number = models.CharField(verbose_name='身份证号', max_length=128, blank=True, null=True)
    phone_number = models.CharField(verbose_name='手机号', max_length=128, blank=True, null=True)

    # 成绩
    major_number = models.IntegerField(verbose_name='专业人数', blank=True, null=True)
    major_rank = models.IntegerField(verbose_name='专业排名', blank=True, null=True)
    class_number = models.IntegerField(verbose_name='班级人数', blank=True, null=True)
    class_rank = models.IntegerField(verbose_name='班级排名', blank=True, null=True)
    english_level = models.CharField(verbose_name='英语水平', max_length=128, blank=True, null=True)

    # 志愿
    degree_choices = (('博士', '博士'), ('硕士', '硕士'))
    institute_choices = (('工物系', '工物系'), ('核研院', '核研院'))
    interest_choices = (('粒子物理实验', '粒子物理实验'), ('粒子物理理论', '粒子物理理论'), ('天体物理', '天体物理'),
                        ('核能科学与工程', '核能科学与工程'), ('裂变能科学与工程', '裂变能科学与工程'),
                        ('核聚变与等离子物理', '核聚变与等离子物理'), ('核燃料循环与材料', '核燃料循环与材料'),
                        ('核技术及应用', '核技术及应用'), ('辐射防护及环境保护', '辐射防护及环境保护'),
                        ('医学物理与工程', '医学物理与工程'), ('安全科学与工程', '安全科学与工程'))
    first_degree = models.CharField(verbose_name='一志愿学位', choices=degree_choices, max_length=128, blank=True,
                                    null=True)
    second_degree = models.CharField(verbose_name='二志愿学位', choices=degree_choices, max_length=128, blank=True,
                                     null=True)
    first_institute = models.CharField(verbose_name='一志愿单位', choices=institute_choices, max_length=128, blank=True,
                                       null=True)
    second_institute = models.CharField(verbose_name='二志愿单位', choices=institute_choices, max_length=128, blank=True,
                                        null=True)
    first_interest = models.CharField(verbose_name='一志愿方向', choices=interest_choices, max_length=128, blank=True,
                                      null=True)
    second_interest = models.CharField(verbose_name='二志愿方向', choices=interest_choices, max_length=128, blank=True,
                                       null=True)
    # 资助申请
    yes_or_no_choices = (('否', '否'), ('是', '是'))
    fund_applied = models.CharField(verbose_name='是否申请资助', choices=yes_or_no_choices, max_length=128, blank=True, null=True)
    fund_application_text = models.TextField(verbose_name='资助申请理由', blank=True, null=True)

    # 其他
    cloth_choices = (('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'))
    cloth_size = models.CharField(verbose_name='服装大小', choices=cloth_choices, max_length=128, blank=True, null=True)

    # 文件
    personal_statement = models.FileField(verbose_name='个人陈述', upload_to='uploads', blank=True, null=True)
    school_report = models.FileField(verbose_name='成绩单', upload_to='uploads', blank=True, null=True)
    other_material = models.FileField(verbose_name='其他材料', upload_to='uploads', blank=True, null=True)

    # 确认提交
    is_confirmed = models.CharField(verbose_name='确认提交', choices=yes_or_no_choices, max_length=128, default='否', blank=True)

    # 初试结果,是否参加夏令营
    check_choices = (('未审核', '未审核'), ('通过', '通过'), ('不通过', '不通过'))
    check_status = models.CharField(verbose_name='根管理员初审', choices=check_choices, max_length=128, default='未审核', blank=True, null=True)
    fund_status = models.CharField(verbose_name='资助审核结果', choices=check_choices, max_length=128, blank=True, null=True)

    dep_check_status = models.CharField(verbose_name='工物系初审', choices=check_choices, max_length=128, default='未审核', blank=True, null=True)
    inet_check_status = models.CharField(verbose_name='核研院初审', choices=check_choices, max_length=128, default='未审核', blank=True, null=True)

    # 复试结果
    retest_grade_choices = (('A1', 'A1'), ('A2', 'A2'), ('B', 'B'), ('C', 'C'), ('未审核', '未审核'))
    dep_retest_grade = models.CharField(verbose_name='工物系复试结果', choices=retest_grade_choices, max_length=128, default='未审核', blank=True, null=True)
    inet_retest_grade = models.CharField(verbose_name='核研院复试结果', choices=retest_grade_choices, max_length=128, default='未审核', blank=True, null=True)

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = '所有报名信息'
