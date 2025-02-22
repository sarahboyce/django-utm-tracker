# Generated by Django 3.1.3 on 2020-11-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("utm_tracker", "0002_leadsource_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leadsource",
            name="medium",
            field=models.CharField(
                help_text="utm_medium: Identifies what type of link was used, such as cost per click or email.",
                max_length=30,
            ),
        ),
    ]
