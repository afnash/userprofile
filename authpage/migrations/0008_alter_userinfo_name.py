# Generated by Django 5.0.6 on 2024-05-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authpage', '0007_alter_userinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
