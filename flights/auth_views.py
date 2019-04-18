from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .serializers import TokenSerializer, UserSerializer
from .decorators import validate_user_registration, validate_user_login


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    
    permission_classes = (permissions.AllowAny,) # This permission class will overide the global permission class setting
    queryset = User.objects.all()
    @validate_user_login
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
      
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer_class = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user))
                })
            serializer_class.is_valid()
            return Response(serializer_class.data)
        error_msg= {"error":"Not Registered, Please register."}
        return Response(error_msg,status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(generics.CreateAPIView):
    """
    POST /register/
    """
    permission_classes = (permissions.AllowAny,)
    @validate_user_registration
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            data=UserSerializer(new_user).data,
            status=status.HTTP_201_CREATED
        )