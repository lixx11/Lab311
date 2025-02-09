# Generated by Django 2.0.2 on 2018-03-10 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], max_length=128, null=True, verbose_name='性别')),
                ('student_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='考生编号')),
                ('phone_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='手机号')),
                ('school', models.CharField(blank=True, max_length=128, null=True, verbose_name='本科毕业学校')),
                ('major', models.CharField(blank=True, max_length=128, null=True, verbose_name='本科专业')),
                ('graduate_year', models.TimeField(blank=True, null=True, verbose_name='本科毕业时间')),
                ('first_institute', models.CharField(blank=True, max_length=128, null=True, verbose_name='原报考院系')),
                ('first_major', models.CharField(blank=True, max_length=128, null=True, verbose_name='原报考专业')),
                ('exam_for_first_institute', models.CharField(blank=True, choices=[('否', '否'), ('是', '是')], max_length=128, null=True, verbose_name='是否参加原报考院系复试')),
                ('politics', models.IntegerField(blank=True, null=True, verbose_name='政治')),
                ('english', models.IntegerField(blank=True, null=True, verbose_name='英语')),
                ('subject3_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='科目三名称')),
                ('subject3_score', models.IntegerField(blank=True, null=True, verbose_name='科目三成绩')),
                ('subject_major_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='专业课名称')),
                ('subject_major_score', models.IntegerField(blank=True, null=True, verbose_name='专业课成绩')),
                ('total_score', models.IntegerField(blank=True, null=True, verbose_name='总分')),
                ('interest1', models.CharField(blank=True, choices=[('核能方向 - 核能与核技术工程（085226）- 清华本部', '核能方向 - 核能与核技术工程（085226）- 清华本部'), ('核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部', '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'), ('核技术方向 - 核能与核技术工程（085226）- 清华本部', '核技术方向 - 核能与核技术工程（085226）- 清华本部'), ('公共安全 - 安全工程（085224） - 深圳研究生院', '公共安全 - 安全工程（085224） - 深圳研究生院'), ('核能安全 - 安全工程（085224） - 深圳研究生院', '核能安全 - 安全工程（085224） - 深圳研究生院')], max_length=8, null=True, verbose_name='第一志愿')),
                ('interest2', models.CharField(blank=True, choices=[('核能方向 - 核能与核技术工程（085226）- 清华本部', '核能方向 - 核能与核技术工程（085226）- 清华本部'), ('核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部', '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'), ('核技术方向 - 核能与核技术工程（085226）- 清华本部', '核技术方向 - 核能与核技术工程（085226）- 清华本部'), ('公共安全 - 安全工程（085224） - 深圳研究生院', '公共安全 - 安全工程（085224） - 深圳研究生院'), ('核能安全 - 安全工程（085224） - 深圳研究生院', '核能安全 - 安全工程（085224） - 深圳研究生院')], max_length=8, null=True, verbose_name='第二志愿')),
                ('interest3', models.CharField(blank=True, choices=[('核能方向 - 核能与核技术工程（085226）- 清华本部', '核能方向 - 核能与核技术工程（085226）- 清华本部'), ('核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部', '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'), ('核技术方向 - 核能与核技术工程（085226）- 清华本部', '核技术方向 - 核能与核技术工程（085226）- 清华本部'), ('公共安全 - 安全工程（085224） - 深圳研究生院', '公共安全 - 安全工程（085224） - 深圳研究生院'), ('核能安全 - 安全工程（085224） - 深圳研究生院', '核能安全 - 安全工程（085224） - 深圳研究生院')], max_length=8, null=True, verbose_name='第三志愿')),
                ('interest4', models.CharField(blank=True, choices=[('核能方向 - 核能与核技术工程（085226）- 清华本部', '核能方向 - 核能与核技术工程（085226）- 清华本部'), ('核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部', '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'), ('核技术方向 - 核能与核技术工程（085226）- 清华本部', '核技术方向 - 核能与核技术工程（085226）- 清华本部'), ('公共安全 - 安全工程（085224） - 深圳研究生院', '公共安全 - 安全工程（085224） - 深圳研究生院'), ('核能安全 - 安全工程（085224） - 深圳研究生院', '核能安全 - 安全工程（085224） - 深圳研究生院')], max_length=8, null=True, verbose_name='第四志愿')),
                ('interest5', models.CharField(blank=True, choices=[('核能方向 - 核能与核技术工程（085226）- 清华本部', '核能方向 - 核能与核技术工程（085226）- 清华本部'), ('核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部', '核燃料方向（定向） - 核能与核技术工程（085226）- 清华本部'), ('核技术方向 - 核能与核技术工程（085226）- 清华本部', '核技术方向 - 核能与核技术工程（085226）- 清华本部'), ('公共安全 - 安全工程（085224） - 深圳研究生院', '公共安全 - 安全工程（085224） - 深圳研究生院'), ('核能安全 - 安全工程（085224） - 深圳研究生院', '核能安全 - 安全工程（085224） - 深圳研究生院')], max_length=8, null=True, verbose_name='第五志愿')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads', verbose_name='所有材料')),
                ('is_confirmed', models.CharField(blank=True, choices=[('否', '否'), ('是', '是')], default='否', max_length=128, verbose_name='确认提交')),
            ],
            options={
                'verbose_name': '调剂信息',
                'verbose_name_plural': '所有调剂信息',
            },
        ),
    ]
