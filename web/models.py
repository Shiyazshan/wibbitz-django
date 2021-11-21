from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField


CONTENT_TYPE = (
    ("bloog_post","Blog Post"),
    ("webinart", "Webinar"),
    ("report","Report")
)

class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Promoter(models.Model): 
    image = models.FileField(upload_to="promoters/")


class Feature(models.Model):
    image = models.ImageField(upload_to="features/")
    icon = models.FileField(upload_to="features/")
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="features/")

    def __str__(self):
        return self.title

class VideoBlog(models.Model):
    image = models.FileField(upload_to="videoblog/")
    title = models.CharField(max_length=128)
    logo = models.FileField(upload_to="videoblog/")

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(max_length=255)
    logo = FileField(upload_to="product/",blank=True,null=True)
    description = models.TextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=128)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MarketingFeature(models.Model):
    image = models.FileField(upload_to="marketingfeature/")
    title = models.CharField(max_length=255)
    description = models.TextField()  

    def __str__(self):
        return self.title

class Product(models.Model):
    logo = FileField(upload_to="product/",blank=True,null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="product/")

    def __str__(self):
        return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to="blog/")
    title = models.CharField(max_length=255)
    content_type = TextField(choices=CONTENT_TYPE)
