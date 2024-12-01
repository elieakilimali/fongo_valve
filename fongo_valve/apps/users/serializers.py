from rest_framework import serializers
from fongo_valve.apps.users.models import CustomerUser

class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('email', 'password', 'role')  # Inclure les champs nécessaires pour l'inscription

    def create(self, validated_data):
        user = CustomerUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', CustomerUser.STUDENT)  # rôle par défaut
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
