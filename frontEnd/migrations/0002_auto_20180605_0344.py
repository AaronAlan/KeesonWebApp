# Generated by Django 2.0.5 on 2018-06-05 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontEnd', '0001_initial'),
    ]

    operations = [
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
    ]
