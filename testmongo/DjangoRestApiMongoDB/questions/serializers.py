from rest_framework import serializers
from .models import Question

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields=('questionId', 'questionLabel', 'questionDataType')