# from django.shortcuts import render, redirect
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

# def images_api(request):
#     images = get_images()
#     serialized_images = [serialized_images(image) for image in images]
#     return JsonResponse({'images': serialized_images})

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
    # else:
    #     form = ImageForm()
    # return render(request, 'upload_image.html', {'form': form})

# class OtheImageUpload(APIView):
#     pass

class ImageListView(APIView):
    def get(self, request):
        images = ImageModel.objects.all()
        # ser_images = ImageSerializer(images)
        serialized_images = [serialize_image(image) for image in images]
        # image_data = images.image_data
        return Response({'images': serialized_images})

class An_Image(APIView):
    def get(self, request, id):
        images = ImageModel.objects.get(id=id)
        # ser_images = ImageSerializer(images)
        image_data = images.image_data
        if images is not None:
            return Response({'image':image_data}, status=status.HTTP_200_OK)
        else:
            return Response("Unable to find your request, please try again", status=status.HTTP_400_BAD_REQUEST)
        
class TokenReq(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    

#BLOB: Binary Large Objects -->SQL, MySQL, postgreSQL doesn't have that
# BYTEA Binary data --> PostgreSQL
# Large Objects also have some security issues since anyone connected to the database can view and/or modify any Large Object, even if they don't have permissions to view/update the row containing the Large Object reference. from 31.7 storing binary data postgresql docs


#code snippets
# function onFileSelect(event) {
#   const reader = new FileReader();
#   img_upload = event.target.files[0];
#   reader.readAsDataURL(event.target.files[0]);
#   setTimeout(function () {
#     img_upload = reader.result;
#     toggle_upload.value = true;
#   }, 2000);
# }

# let profile_picture = ref("");
# function getUserImage() {
#   const dec = new TextDecoder("utf-8");
#   fetchUser(user.email).then((response) => {
#     let img = response.img.data;
#     profile_picture.value = dec.decode(new Uint8Array(img));
#   });
# }