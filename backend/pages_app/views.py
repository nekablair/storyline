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

    def get(self, request, id):
        pages = Page.objects.get(id=id)
        ser_page = PageSerializer(pages)
        if ser_page:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class A_page(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self, request, id):
        ser_page = PageSerializer(data=request.data)
        if ser_page.is_valid():
            ser_page.save()
            return Response(ser_page, status=status.HTTP_201_CREATED)
        return Response("Bad request :", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        page = Page.objects.get(id=id)
        ser_page = PageSerializer
        if ser_page:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
