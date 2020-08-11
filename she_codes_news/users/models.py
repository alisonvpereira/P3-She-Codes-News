from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.urls import reverse


class CustomUser(AbstractUser):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True, default='yyyy-mm-dd')
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('users:user-detail', args=[str(self.id)])
    
    def get_update_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user_update', args=[str(self.id)])
    
    # def get_delete_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('author_delete', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    # def __str__(self):
    #     return self.username

