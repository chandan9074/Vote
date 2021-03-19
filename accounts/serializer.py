from rest_framework import serializers
from .models import UserProfile


from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "username", "password"]

    def create(self, validated_data):
        first_name = validated_data.pop("first_name", "")
        last_name = validated_data.pop("last_name", "")
        username = validated_data.pop("username")
        email = validated_data.pop("email", "")
        password = validated_data.pop("password", "")

        user = UserProfile.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
        return user