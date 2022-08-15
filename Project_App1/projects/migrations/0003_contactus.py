# Generated by Django 4.1 on 2022-08-15 16:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contactus",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("project_name", models.CharField(max_length=200)),
                ("project_details", models.TextField(max_length=2000)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
