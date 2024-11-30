from rest_framework import serializers
from fongo_valve.apps.users.models import CustomerUser

class CustomerUserSerializer(serializers.ModelSerializer):
    model = CustomerUser
    fields = ["id","username","role","departement"]
    extra_kwargs = {"password": {"write_only":True}}

    def create(self,validation_data):
        user = CustomerUser.objects.create_user(
            username=validation_data['username'],
            email=validation_data['email'],
            password=validation_data['password'],
            role = validation_data['role'],
            department = validation_data.get['department','']

        )

        return user
    