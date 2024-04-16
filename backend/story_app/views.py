from django.shortcuts import render, get_object_or_404
from story_app.models import Story
from .form import StoryForm
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# from .utils import generate_story
from django.http import JsonResponse, HttpResponse
from .utils import get_short_story, generate_story
from image_app.views import An_Image
from image_app.image_generation import save_image
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser





# from django.shortcuts import render, get_object_or_404
# from story_app.models import Story
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from .serializers import StorySerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from .story_generation import generate_story
# from django.http import JsonResponse

def generate_story_from_words(request):
    words = request.GET.get('words') # Extract the expected words from the request
    story = generate_story(words) # Call the generate_story function with the extracted words
    return JsonResponse({'story': story}) # Return the story as a JSON response

class StoryUploadView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def post(self, request):    
        print(request.data)
        serializer = StorySerializer(data=request.data)
        # if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid() & serializer.is_valid():
            form.save()
            serializer.save()
                # return redirect('image_list')
            return Response({'message' : 'Story uploaded successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Failed to upload story'}, status=status.HTTP_400_BAD_REQUEST)

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























# def generate_story_from_words(request):
#     # context = {}
#     # if request.method == 'POST':
#     #     user_input = request.POST.get('user_input', '')
#     #     chat_history = request.POST.get('chat_history')
#     #     words = f"{chat_history}\nUser:{user_input}\nChatGPT:" 
#     #     response = generate_story(words)
#     #     context['chat_history'] = f'{chat_history}\nUser:{user_input}\nChatGPT:{response}'
#     #     return render(request, 'chatapp/')

#     print("string request line 13", request)
#     words = request.GET.get('words') # Extract the expected words from the request
#     print("Views line 14", words)
#     story = generate_story(words) # Call the generate_story function with the extracted words
#     return HttpResponse({'story': story}) # Return the story as a JSON response

# Create your views here.

# def generate_story_from_request(request):
#     # Define your words here or fetch them from somewhere
#         # return get_short_story(request)

#     response = HttpResponse("Some content")

#     # Set the CORS headers to allow requests from http://localhost:5173
#     response["Access-Control-Allow-Origin"] = "http://localhost:5173"
#     response["Access-Control-Allow-Credentials"] = "true"
    
#     # Optionally, set other CORS headers as needed
#     # response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
#     # response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

#     return response


# class All_Stories(APIView):
#     def get(self, request):
#         stories = Story.objects.all()
#         serializer = StorySerializer(stories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class A_Story(APIView):
#     def get(self, request, story_id):
#         story = get_object_or_404(Story, id=story_id)
#         serializer = StorySerializer(story)
#         return Response(serializer.data)

#     def put(self, request, story_id):
#         story = get_object_or_404(Story, id=story_id)
#         serializer = StorySerializer(story, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def post(self, request):
#         data = Story(request)
#         ai_image = An_Image(data["words"])
#         print(ai_image)
#         new_image = save_image(ai_image)
#         # return new_image
#         return HttpResponse({"image_url": new_image})

#     def delete(self, request, story_id):
#         story = get_object_or_404(Story, id=story_id)
#         story.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    