# Generated by Django 2.0.3 on 2018-08-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20180821_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officebearers',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]