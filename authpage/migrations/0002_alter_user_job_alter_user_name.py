# Generated by Django 5.0.6 on 2024-05-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
