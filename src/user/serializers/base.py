from rest_framework import serializers

from user.models.base import User

from file.serializers import FileSerializer


class UserSerializer(serializers.ModelSerializer):
    profile_picture = FileSerializer()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'role',
            'profile_picture',
            ]
