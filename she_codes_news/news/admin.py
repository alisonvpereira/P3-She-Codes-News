from django.contrib import admin
from .models import NewsStory, Category

admin.site.register(Category)

@admin.register(NewsStory)
class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ['author_id', 'title', 'status', 'author', 'display_category', 'created_on', 'pub_date']
    list_filter = ("category","status","author",)
    search_fields = ['title', 'content']

