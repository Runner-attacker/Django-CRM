# Generated by Django 5.1.1 on 2024-09-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="status",
            field=models.CharField(default="Active", max_length=10),
        ),
    ]
