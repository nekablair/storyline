from django.db import models
from story_app.models import Story
from image_app.models import ImageModel

# Create your models here.
class Page(models.Model):
    story_text = models.TextField()
    image_data = models.ForeignKey(ImageModel, on_delete=models.CASCADE, related_name='pages_image')
    book_id = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='pages_book_id')#one to many (one book, many pages)

    # using indexing to be able to grab information quicker and because I will be querying for that often with the stories
    class Meta: #getting column "story_text does not exist"
        indexes = [
            models.Index(fields=['story_text']),
            models.Index(fields=['image_data'])
        ]
