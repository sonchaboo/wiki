from django.contrib import admin

from .models import Oblast, Category, Article
# Register your models here.

admin.site.register(Oblast)
admin.site.register(Category)
admin.site.register(Article)