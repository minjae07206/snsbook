# Generated by Django 5.0.1 on 2024-02-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0003_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="caption",
            field=models.TextField(default=""),
        ),
    ]
