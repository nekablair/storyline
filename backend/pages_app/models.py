from django.db import models
from story_app.models import Story

# Create your models here.
class Page(models.Model):
    page_id = models.IntegerField()
    book_id = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='pages')#one to many (one book, many pages)

