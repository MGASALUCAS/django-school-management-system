# Generated by Django 4.1 on 2022-08-29 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("academic", "0002_initial"),
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentAttendance",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.IntegerField(default=0)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "class_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academic.classregistration",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student.enrolledstudent",
                    ),
                ),
            ],
            options={"unique_together": {("student", "date")},},
        ),
    ]
