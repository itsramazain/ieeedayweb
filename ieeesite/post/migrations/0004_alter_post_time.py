# Generated by Django 4.1 on 2022-10-06 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_post_delete_posts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
