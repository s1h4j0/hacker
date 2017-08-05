from django.contrib import admin
from .models import Category, CategoryDetail, Subject


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'need']


@admin.register(CategoryDetail)
class CategoryDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'need', 'category']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'need', 'category_detail']
