# Generated by Django 4.0.5 on 2022-06-15 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_rename_upldated_report_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
    ]
