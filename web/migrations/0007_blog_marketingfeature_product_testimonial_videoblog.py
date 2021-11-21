# Generated by Django 3.2.9 on 2021-11-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/')),
                ('title', models.CharField(max_length=255)),
                ('content_type', models.TextField(choices=[('bloog_post', 'Blog Post'), ('webinart', 'Webinar'), ('report', 'Report')])),
            ],
        ),
        migrations.CreateModel(
            name='MarketingFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='marketingfeature/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.FileField(blank=True, null=True, upload_to='product/')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='')),
                ('logo', models.FileField(blank=True, null=True, upload_to='product/')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='VideoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='videoblog/')),
                ('title', models.CharField(max_length=128)),
                ('logo', models.FileField(upload_to='videoblog/')),
            ],
        ),
    ]
