from rest_framework import serializers
from .models import Quiz

# Este serializador convierte instancias del modelo Quiz en formatos como JSON para la API RESTful.
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at']