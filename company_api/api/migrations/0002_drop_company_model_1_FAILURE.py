# Generated by Django 5.2.1 on 2025-05-18 01:51

from django.db import migrations, models


# def drop_company_model(apps, schema_editor):
#     schema_editor.execute("DROP TABLE IF EXISTS Company;")       # Custom SQL to drop table


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_create_company_model'),
    ]

    operations = [
        # migrations.SeparateDatabaseAndState(
        #     database_operations=[migrations.RunPython(drop_company_model)],
        #     state_operations=[
        #         migrations.DeleteModel('Company'),
        #     ]
        # )
    ]
