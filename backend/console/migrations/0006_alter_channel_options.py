# Generated by Django 5.2 on 2025-05-03 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0005_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'managed': False},
        ),
    ]
