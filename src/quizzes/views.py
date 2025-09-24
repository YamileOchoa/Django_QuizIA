from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizSerializer

# ViewSet básico para el modelo Quiz
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
