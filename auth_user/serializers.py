from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели CustomUser."""

    class Meta:
        model = CustomUser
        fields = ['email', ]


class ConfirmationSerializer(serializers.Serializer):
    """Сериалайзер для views авторизации, выдача JWT-token."""

    class Meta:
        model = CustomUser
        fields = ['email', 'confirmation_code']


class APIUserSerializer(serializers.ModelSerializer):
    """Сериалайзер для views создания и редактирования профиля."""

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'username', 'bio', 'email', 'role']
