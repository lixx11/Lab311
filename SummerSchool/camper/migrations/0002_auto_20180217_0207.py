# Generated by Django 2.0.2 on 2018-02-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_confirmed',
            field=models.CharField(blank=True, choices=[('N', '否'), ('Y', '是')], default='N', max_length=128, verbose_name='确认提交'),
        ),
    ]