from django.contrib.auth import get_user_model
from django.db import models


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.CharField(max_length=2000, default = "https://picsum.photos/600")
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title