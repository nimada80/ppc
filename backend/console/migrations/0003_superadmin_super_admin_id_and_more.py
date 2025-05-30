# Generated by Django 5.2 on 2025-04-30 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("console", "0002_superadmin"),
    ]

    operations = [
        migrations.AddField(
            model_name="superadmin",
            name="super_admin_id",
            field=models.PositiveIntegerField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="superadmin",
            name="admin_super_password",
            field=models.CharField(max_length=128, verbose_name="Super Admin password"),
        ),
        migrations.AlterField(
            model_name="superadmin",
            name="admin_super_user",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="Super Admin name"
            ),
        ),
        migrations.AlterField(
            model_name="superadmin",
            name="user_count",
            field=models.PositiveIntegerField(default=0, verbose_name="User Count"),
        ),
        migrations.AlterField(
            model_name="superadmin",
            name="user_limit",
            field=models.PositiveIntegerField(verbose_name="User Limit"),
        ),
    ]
