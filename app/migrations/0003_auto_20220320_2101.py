# Generated by Django 3.1.3 on 2022-03-21 02:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20220320_2059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='communitiy',
            new_name='communities',
        ),
        migrations.RenameField(
            model_name='communities',
            old_name='communities',
            new_name='community',
        ),
    ]
