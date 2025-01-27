from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CV
from .serializers import CVSerializer

class CVViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CVSerializer

    def get_queryset(self):
        return CV.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
