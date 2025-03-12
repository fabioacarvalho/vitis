# Generated by Django 4.2.19 on 2025-03-12 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Name")),
                (
                    "url",
                    models.CharField(
                        help_text="Set model and app or your custom URL, for example: app.model or extra/content/",
                        max_length=300,
                        verbose_name="URL",
                    ),
                ),
                (
                    "admin",
                    models.BooleanField(default=False, verbose_name="Administrative"),
                ),
                ("support", models.BooleanField(default=False, verbose_name="Support")),
                (
                    "icon",
                    models.CharField(
                        default="fi-rr-angle-small-right",
                        help_text="Set the name for the desired icon based on FlatIcon, for example 'fi-rr-angle-small-right'",
                        max_length=300,
                        verbose_name="Icon class name",
                    ),
                ),
                ("order", models.IntegerField(default=0, verbose_name="Order")),
                ("active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "father",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.menu",
                    ),
                ),
            ],
            options={
                "verbose_name": "Menu",
                "verbose_name_plural": "Menus",
            },
        ),
    ]
