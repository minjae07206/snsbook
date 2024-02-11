from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import datetime
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images')
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField(default="")
    image = models.ImageField(upload_to="post_images")
    created_time = models.DateTimeField(default=datetime.now)
    number_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user
    
