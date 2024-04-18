from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# (
#     HTTP_200_OK,
#     HTTP_201_CREATED,
#     HTTP_404_NOT_FOUND,
#     HTTP_204_NO_CONTENT,
#     HTTP_400_BAD_REQUEST
# )
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class Sign_up(APIView):
    def post(self, request):
        data = request.data.copy()
        data["username"] = request.data.get("email")        
        new_user = User(**data)
        try :
            new_user.full_clean()
            new_user.save()
            new_user.set_password(data.get("password"))
            new_user.save()
            login(request, new_user)
            token = Token.objects.create(user = new_user)
            return Response({'user':new_user.display_name, "token":token.key}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            print(e)
            return Response(e.messages, status=status.HTTP_400_BAD_REQUEST)

class Log_in(APIView):
    def post(self, request):
        data = request.data.copy()
        data["username"] = request.data.get("username", request.data.get("email")) 
        # email = request.data.get("email")
        # password = request.data.get("password")
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({ "user": user.display_name, "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response("No user matching credentials", status=status.HTTP_404_NOT_FOUND)
            

class TokenReq(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class Log_out(TokenReq):

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Info(TokenReq):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     return Response({"email": request.user.email})
    
    def put(self, request):
        try:
            data = request.data.copy()
            ruser = request.user
            ruser.display_name = data.get("display_name", ruser.display_name)
            cur_password = data.get("password")
            if cur_password and data.get("new_password"):
                auth_user = authenticate(username = ruser.username, password = cur_password)
                if auth_user == ruser:
                    ruser.set_password(data.get("new_password"))
            ruser.full_clean() #using this since we aren't using serializers, otherwise would be using is_valid()
            ruser.save()
            return Response({"display_name": ruser.display_name}, status=status.HTTP_200_OK)
        except ValidationError as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    
