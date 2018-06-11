# Generated by Django 2.0.5 on 2018-06-11 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0005_auto_20180607_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientex',
            name='med_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='用药名称'),
        ),
        migrations.AlterField(
            model_name='dm_ronghua',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '男性'), ('F', '女性')], max_length=64, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '男性'), ('F', '女性')], max_length=64, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='patientex',
            name='dose',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='每次用药剂量'),
        ),
        migrations.AlterField(
            model_name='patientpe',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='体格检查名称'),
        ),
        migrations.AlterField(
            model_name='patientpe',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='体格检查日期'),
        ),
        migrations.AlterField(
            model_name='patientpe',
            name='result',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='体格检查结果'),
        ),
    ]
