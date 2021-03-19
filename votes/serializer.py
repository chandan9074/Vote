from rest_framework import serializers

from .models import PublicPoll, PrivatePoll, PrivatePollOption, PublicPollOption, PublicPollResult, PrivatePollResult
from accounts.models import UserProfile

class PublicPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPoll
        fields = "__all__"


class PrivatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivatePoll
        fields = "__all__"


class PrivatePollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivatePollOption
        fields = "__all__"


class PublicPollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPollOption
        fields = "__all__"

class UserPublicPollSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicPoll
        fields = ["user_profile"]

class PublicPollResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPollResult
        fields = "__all__"

class PrivatePollResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivatePollResult
        fields = "__all__"

class PrivatePollRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivatePoll
        fields = ["password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"