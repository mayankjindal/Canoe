# Generated by Django 2.1 on 2018-08-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_event_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]