# Generated by Django 5.0.6 on 2024-05-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authpage', '0003_alter_user_age_alter_user_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='userinfo',
        ),
    ]
