# Generated by Django 5.0.1 on 2024-02-02 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='title',
            new_name='job_title',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='years',
            new_name='years_with_company',
        ),
    ]
