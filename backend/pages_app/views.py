from django.shortcuts import render
from .models import Page
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class All_pages(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        # pages = Page.objects.get(id=id)
        pages = Page.objects.all()
        ser_pages = PageSerializer(pages, many=True)
        # ser_pages = [PageSerializer(pages) for page in pages]
        # serialized_images = [serialize_image(image) for image in images]
        if ser_pages:
            # return Response({'images': serialized_images})
            return Response({'pages': ser_pages.data}, status=status.HTTP_200_OK)
        return Response({'Error': 'No pages available'}, status=status.HTTP_400_BAD_REQUEST)

class A_page(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self, request, id):
        ser_page = PageSerializer(data=request.data)
        if ser_page.is_valid():
            ser_page.save()
            return Response(ser_page.data, status=status.HTTP_201_CREATED)
        return Response({'Bad request':'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        try:
            page = Page.objects.get(id=id)
            ser_page = PageSerializer(page)
            # if ser_page:
            # return Response(status=status.HTTP_200_OK)
            return Response(ser_page.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Page does not exist'}, status=status.HTTP_404_NOT_FOUND)
