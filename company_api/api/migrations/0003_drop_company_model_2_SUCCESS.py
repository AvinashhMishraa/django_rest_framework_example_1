# Generated by Django 5.2.1 on 2025-05-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_drop_company_model_1_FAILURE'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]


