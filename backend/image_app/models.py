from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    # return {filename}.format(filename=filename)
    return f"media/{filename}"

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=150)
    image_data = models.ImageField(_("Image"), upload_to='media/')
    image_binary = models.BinaryField(default=b'')


    def __str__(self):
        return self.name
    