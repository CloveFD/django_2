# Generated by Django 4.0.5 on 2022-06-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='no_picture.png', upload_to='customers'),
        ),
    ]