# Generated by Django 2.2.2 on 2020-04-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0008_auto_20200427_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='exam_for_first_institute',
            field=models.CharField(blank=True, choices=[('不参加', '不参加'), ('参加', '参加')], max_length=128, null=True, verbose_name='是否参加原报考院系复试'),
        ),
    ]