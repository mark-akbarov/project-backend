from rest_framework import serializers

from user.models.passport import PassportVerification


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
