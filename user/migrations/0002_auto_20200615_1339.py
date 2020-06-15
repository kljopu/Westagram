# Generated by Django 3.0.7 on 2020-06-15 04:39

from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='가입일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='이름'),
        ),
    ]