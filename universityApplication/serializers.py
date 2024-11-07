from rest_framework import serializers
from universityApplication.models import personalStatusForm

class personalStatusFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = personalStatusForm
        fields = '__all__'