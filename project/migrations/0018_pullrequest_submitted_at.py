# Generated by Django 3.2.7 on 2021-09-15 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20210914_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='submitted_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submitted At'),
        ),
    ]
