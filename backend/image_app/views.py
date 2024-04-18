from .form import ImageForm
from .models import ImageModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ImageSerializer, AllImageSerializer, serialize_image
from .image_generation import get_generated_images, save_image
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from django.http import JsonResponse, HttpResponse
import io
import requests
from PIL import Image
import base64

def generate_images_from_text(request):
    text = request.POST.get('text')
    images = get_generated_images(text)
    print(images)
    return HttpResponse({'images': images})

def process_image_to_base64(url):
    response = requests.get(url)
    image_bytes = io.BytesIO(response.content)
    img = Image.open(image_bytes)
    jpeg_image = io.BytesIO()
    img.save(jpeg_image, format='JPEG')
    jpeg_image.seek(0)
    base64_string = base64.b64encode(jpeg_image.read()).decode('ascii')
    return "data:image/jpeg;base64," + base64_string

class TokenReq(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class ImageUploadView(TokenReq):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def post(self, request):    
        print(request.data)
        # url = request.data.get('url')
        # process_image_to_base64(url)
        save_image()
        # ser_url = url.serialize_image
        # print(ser_url)
        serializer = ImageSerializer(data=request.data)
        # if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid() & serializer.is_valid():
            form.save()
            serializer.save()
                # return redirect('image_list')
            return Response({'message' : 'Image uploaded successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Failed to upload image'}, status=status.HTTP_400_BAD_REQUEST)

class ImageListView(APIView):
    def get(self, request):
        images = ImageModel.objects.all()
        serialized_images = [serialize_image(image) for image in images]
        return Response({'images': serialized_images})

class An_Image(APIView):
    def post(self, request, id):
        images = ImageModel.objects.get(id=id)
        ser_images = serialize_image(images)
        image_data = ser_images
        print(image_data)
        if images is not None:
            return Response({'image':image_data}, status=status.HTTP_200_OK)
        else:
            return Response("Unable to find your request, please try again", status=status.HTTP_400_BAD_REQUEST)
        

