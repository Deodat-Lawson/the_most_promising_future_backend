import jwt
from django.db.models.functions import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ValidationError
import datetime


# Create your views here.
class RegisterView(APIView):
  def post(self, request):
    print("Received request")
    print('Request method:', request.method)
    print("Request data:", request.data)

    email = request.data.get('email')
    if not email:
      raise ValidationError('Email is required.')
    print(f"Email: {email}")

    if User.objects.filter(email=email).exists():
      print(f"User with email {email} already exists.")
      raise ValidationError('A user with this email already exists.')

    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
      print("Validation errors:", serializer.errors)
      raise ValidationError(serializer.errors)

    print(f"Validated data: {serializer.validated_data}")
    serializer.save()

    # Check if the user is saved in the database
    if User.objects.filter(email=email).exists():
      print(f"User with email {email} saved successfully.")
    else:
      print(f"Failed to save user with email {email}.")

    return Response(serializer.data)


class LoginView(APIView):
  def post(self, request):
    print("Received request for login")
    username = request.data.get('username')
    password = request.data.get('password')
    print(username, password)
    user = User.objects.filter(username=username).first()
    if user is None:
      raise AuthenticationFailed('User not found')
    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect password')

    payload = {
      'id': user.id,
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      'iat': datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    print(f"Token: {token}")
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
      'jwt': token,
      'username': username
    }

    if user:
      print(f'User {username} logged in successfully')
    else:
      print('User login failed')
    return response

class UserView(APIView):
  def get(self, request):
    token = request.COOKIES.get('jwt')
    if not token:
      raise AuthenticationFailed('Unauthenticated')

    try:
      payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthenticated')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)

class LogoutView(APIView):
  def post(self, request):
    print("Received request for logout")
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message': 'success'
    }
    return response





