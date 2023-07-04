from rest_framework import serializers

from user.models.passport_verification import PassportVerification


class PassportVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportVerification
        fields = [            
            'id',
            'user',
            'image',
            'serial_number',
            'pinfl',
            ]
