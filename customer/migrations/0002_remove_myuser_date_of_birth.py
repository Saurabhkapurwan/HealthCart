# Generated by Django 5.0.3 on 2024-03-29 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="myuser",
            name="date_of_birth",
        ),
    ]