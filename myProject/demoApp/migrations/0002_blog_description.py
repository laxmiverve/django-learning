# Generated by Django 5.0.7 on 2024-07-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
