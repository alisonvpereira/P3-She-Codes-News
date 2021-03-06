from django.contrib.auth import get_user_model
from django.db import models
from users.models import CustomUser
from django.urls import reverse


DRAFT = 0
PUBLISH = 1

STATUS = (
    (DRAFT,"Draft"),
    (PUBLISH,"Publish")
)

class Category(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a category')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        CustomUser,on_delete=models.CASCADE,related_name="stories")
    pub_date = models.DateTimeField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    image_url = models.CharField(max_length=2000, default = "https://picsum.photos/600")
    category = models.ManyToManyField(Category, help_text='Select a category for this story')
  
    
    class Meta:
        ordering = ['-status', '-pub_date']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('news:story', args=[str(self.id)])
    
    def get_update_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('story_update', args=[str(self.id)])

    def __str__(self):
        return self.title

    
    def display_category(self):
        """Create a string for the Category. This is required to display genre in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'




