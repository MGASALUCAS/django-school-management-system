# Generated by Django 4.1 on 2022-08-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0012_auto_20200419_1255"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academicinfo",
            name="registration_no",
            field=models.IntegerField(default=775877, unique=True),
        ),
    ]