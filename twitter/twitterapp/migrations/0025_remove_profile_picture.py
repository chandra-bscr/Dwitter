# Generated by Django 4.2.1 on 2023-05-30 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0024_remove_profile_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
