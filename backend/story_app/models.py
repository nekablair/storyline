from django.db import models
from image_app.models import ImageModel
from user_app.models import User

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=30, default='fiction')
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    favorites = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id =models.ForeignKey(ImageModel, on_delete=models.CASCADE, default=5)

    