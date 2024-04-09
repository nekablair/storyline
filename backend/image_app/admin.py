from django.contrib import admin
from .models import ImageModel

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',) #adding id

# Register your models here.
admin.site.register(ImageModel, ImageAdmin)
