from django.contrib import admin
from .models import NewsStory

class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author','created_on', 'pub_date']
    list_filter = ("status","author",)
    search_fields = ['title', 'content']

admin.site.register(NewsStory, NewsStoryAdmin)