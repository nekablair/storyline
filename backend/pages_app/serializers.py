from rest_framework.serializers import ModelSerializer
from .models import Page

class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ['page_id', 'book_id']
