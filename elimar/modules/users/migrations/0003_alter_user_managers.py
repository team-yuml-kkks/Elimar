# Generated by Django 4.1.5 on 2023-02-19 10:46

from django.db import migrations
import elimar.modules.users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_username_alter_user_email"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", elimar.modules.users.models.UserManager()),
            ],
        ),
    ]
