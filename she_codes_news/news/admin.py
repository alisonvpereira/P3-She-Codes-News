from django.contrib import admin

# Register your models here.
from .models import NewsStory

@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
    pass