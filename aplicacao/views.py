from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    def get(self, request):
        cursos =Curso.objects.all()
        serializer = CursoSerializer(cursos, many= True)
        return Response('olá')
class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes =Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many= True)
        return Response(serializer.data)