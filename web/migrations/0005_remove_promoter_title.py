# Generated by Django 3.2.9 on 2021-11-20 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_promoter_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promoter',
            name='title',
        ),
    ]
