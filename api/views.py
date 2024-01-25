from rest_framework import viewsets,permissions
from .models import Programador
from .serializer import ProgramadorSerializer
# Create your views here.

class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.all()
    serializer_class = ProgramadorSerializer
    #permission_classes = [permissions.IsAuthenticated]