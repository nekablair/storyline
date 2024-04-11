from django.shortcuts import render, get_object_or_404
from story_app.models import Story
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .story_generation import generate_story
from django.http import JsonResponse

def generate_story_from_words(request):
    words = request.GET.get('words') # Extract the expected words from the request
    story = generate_story(words) # Call the generate_story function with the extracted words
    return JsonResponse({'story': story}) # Return the story as a JSON response



# Create your views here.
class All_Stories(APIView):
    def get(self, request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class A_Story(APIView):
    def get(self, request, story_id):
        story = get_object_or_404(Story, id=story_id)
        serializer = StorySerializer(story)
        return Response(serializer.data)

    def put(self, request, story_id):
        story = get_object_or_404(Story, id=story_id)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, story_id):
        story = get_object_or_404(Story, id=story_id)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    