# Generated by Django 4.1 on 2022-10-06 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("post", "0009_remove_post_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("position", models.CharField(blank=True, max_length=200)),
                ("massage", models.TextField(blank=True, default="")),
                ("time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="person",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="post.group"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="rate",
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
                ("rate", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(name="Post",),
        migrations.AddField(
            model_name="posts",
            name="stars",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person",
                to="post.rate",
            ),
        ),
    ]