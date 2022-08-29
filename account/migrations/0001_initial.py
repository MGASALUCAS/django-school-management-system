# Generated by Django 4.1 on 2022-08-29 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("name", models.CharField(max_length=45)),
                ("photo", models.ImageField(upload_to="admin/")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                (
                    "employee_type",
                    models.CharField(
                        choices=[
                            ("admin", "Admin"),
                            ("professor", "Professor"),
                            ("teacher", "Teacher"),
                            ("register", "Register"),
                            ("student", "Student"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
