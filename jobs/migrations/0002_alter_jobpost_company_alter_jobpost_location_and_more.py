# Generated by Django 5.1.7 on 2025-04-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobpost",
            name="company",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="location",
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="salary",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="jobpost",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
