from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Oblast(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, default='')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, default='')
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.oblast}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, default='')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"



