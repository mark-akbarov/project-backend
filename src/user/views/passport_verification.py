from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from user.serializers.passport_verification import PassportVerificationSerializer
from user.models.passport_verification import PassportVerification
from user.models.base import User


class PassportVerificationViewSet(ModelViewSet):
    queryset = PassportVerification.objects.all()
    serializer_class = PassportVerificationSerializer
    
    def perform_create(self, serializer):
        self.request.user.is_passport_verified = True
        self.request.user.save()
        serializer.save() 
