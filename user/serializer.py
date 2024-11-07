from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=100)
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    print("validated data", validated_data)
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance