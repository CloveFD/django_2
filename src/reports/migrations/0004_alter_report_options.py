# Generated by Django 4.0.5 on 2022-06-17 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_remove_report_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('created',)},
        ),
    ]
