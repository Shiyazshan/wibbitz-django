# Generated by Django 3.2.9 on 2021-11-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20211122_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoter',
            name='white_logo',
            field=models.FileField(blank=True, null=True, upload_to='promoters/'),
        ),
    ]