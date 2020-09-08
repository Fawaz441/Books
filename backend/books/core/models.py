from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.first_name + ' ' +  self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50,unique=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date = models.DateField() 
    slug = models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)