from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    descrition = models.CharField(max_length=250)
    created_at = models.DateTimeField()
