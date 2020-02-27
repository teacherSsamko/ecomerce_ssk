# Generated by Django 3.0.3 on 2020-02-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]