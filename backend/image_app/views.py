from .form import ImageForm
from .models import ImageModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ImageSerializer, AllImageSerializer, serialize_image
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from django.http import JsonResponse

class ImageUploadView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def post(self, request):    
        print(request.data)
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
    def get(self, request, id):
        images = ImageModel.objects.get(id=id)
        ser_images = serialize_image(images)
        image_data = ser_images
        if images is not None:
            return Response({'image':image_data}, status=status.HTTP_200_OK)
        else:
            return Response("Unable to find your request, please try again", status=status.HTTP_400_BAD_REQUEST)
        
class TokenReq(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
