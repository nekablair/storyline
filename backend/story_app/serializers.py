from rest_framework import serializers
from .models import Story
from pages_app.serializers import PageSerializer

class StorySerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = '__all__'