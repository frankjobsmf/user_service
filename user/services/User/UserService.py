#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#django
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

#serializers
from .userSerializers import (
    UserSerializer,
)

#get
class UserProfile(APIView):
    def get(self, request, id):
        
        user_get = User.objects.get(id=id)
        
        user = UserSerializer(user_get)
        
        return Response({
            "user": user.data
        })
        
#post
class Register(APIView):
    def post(self, request, *args, **kwargs):
        
        user_dict = self.request.data['user_dict']
        
        User.objects.create_user(
            username=user_dict['username'],
            email=user_dict['email'],
            password=user_dict['password']
        )
        
        return Response({
            "message": "Registro realizado con exito",
            "status_code": status.HTTP_201_CREATED
        })

class Login(APIView):
    def post(self, request, *args, **kwargs):
        
        user_dict = self.request.data['user_dict']

        print(user_dict)

        user_get = authenticate(username=user_dict['username'], password=user_dict['password'])


        if user_get is None:
            return Response({
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            })

        user = UserSerializer(user_get)
        

        return Response({
            "user": user.data,
            "status_code": status.HTTP_200_OK
        })

class FindUsername(APIView):
    def post(self, request, *args, **kwargs):

        username_post = self.request.data['user_username']

        try:
            user_found = User.objects.get(username=username_post)

            if user_found is None:
                return Response({
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
                })

            user = UserSerializer(user_found)

            return Response({
                "user": user.data,
                "status_code": status.HTTP_200_OK
            })

        except User.DoesNotExist:
            return None