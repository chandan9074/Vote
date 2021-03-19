from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from accounts.models import UserProfile

from .models import (
    PublicPoll,
    PublicPollOption,
    PrivatePoll,
    PrivatePollOption,
    PublicPollResult,
    PrivatePollResult,
)
from .serializer import (
    PublicPollSerializer,
    PrivatePollSerializer,
    PrivatePollOptionSerializer,
    PublicPollOptionSerializer,
    UserPublicPollSerializer,
    PublicPollResultSerializer,
    PrivatePollResultSerializer,
    PrivatePollRequestSerializer,
    UserProfileSerializer,
)

# Create your views here.


class PublicPollView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer_data = PublicPoll.objects.all()
        serializer = PublicPollSerializer(serializer_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicPollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicPollDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPoll.objects.filter(pk=pk)).exists():
            serializer_data = PublicPoll.objects.get(pk=pk)
            serializer = PublicPollSerializer(serializer_data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if (PublicPoll.objects.filter(pk=pk)).exists():
            serializer_data = PublicPoll.objects.get(pk=pk)
            serializer = PublicPollSerializer(serializer_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if (PublicPoll.objects.filter(pk=pk)).exists():
            serializer_data = PublicPoll.objects.get(pk=pk)
            serializer_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PrivatePollView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer_data = PrivatePoll.objects.all()
        serializer = PrivatePollSerializer(serializer_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrivatePollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivatePollDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePoll.objects.filter(pk=pk)).exists():
            serializer_data = PrivatePoll.objects.get(pk=pk)
            serializer = PrivatePollSerializer(serializer_data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if (PrivatePoll.objects.filter(pk=pk)).exists():
            serializer_data = PrivatePoll.objects.get(pk=pk)
            serializer = PrivatePollSerializer(serializer_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if (PrivatePoll.objects.filter(pk=pk)).exists():
            serializer_data = PrivatePoll.objects.get(pk=pk)
            serializer_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublicPollOptionView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer_data = PublicPollOption.objects.all()
        serializer = PublicPollOptionSerializer(serializer_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicPollOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PrivatePollOptionView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer_data = PrivatePollOption.objects.all()
        serializer = PrivatePollOptionSerializer(serializer_data)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrivatePollOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPublicPollSerializerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPoll.objects.filter(user_profile=pk)).exists():
            serializer_data = PublicPoll.objects.filter(user_profile=pk)
            serializer = PublicPollSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if (PublicPoll.objects.filter(pk=pk)).exists():
            serializer_data = PublicPoll.objects.filter(pk=pk)
            serializer_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SpecificPublicPollOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollOption.objects.filter(publicpoll=pk)).exists():
            serializer_data = PublicPollOption.objects.filter(publicpoll=pk)
            serializer = PublicPollOptionSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class UserPrivatePollSerializerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePoll.objects.filter(user_profile=pk)).exists():
            serializer_data = PrivatePoll.objects.filter(user_profile=pk)
            serializer = PrivatePollSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if (PrivatePoll.objects.filter(pk=pk)).exists():
            serializer_data = PrivatePoll.objects.filter(pk=pk)
            serializer_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SpecificPrivatePollOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollOption.objects.filter(privatepoll=pk)).exists():
            serializer_data = PrivatePollOption.objects.filter(privatepoll=pk)
            serializer = PrivatePollOptionSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublicPollResultView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PublicPollResultSerializer(data=request.data)
        if serializer.is_valid():
            public_poll = serializer.validated_data["publicpoll"]
            u_profile = serializer.validated_data["user_profile"]

            if (
                PublicPollResult.objects.filter(
                    publicpoll=public_poll, user_profile=u_profile
                )
            ).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PrivatePollResultView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PrivatePollResultSerializer(data=request.data)
        if serializer.is_valid():
            private_poll = serializer.validated_data["privatepoll"]
            u_profile = serializer.validated_data["user_profile"]

            if (
                PrivatePollResult.objects.filter(
                    privatepoll=private_poll, user_profile=u_profile
                )
            ).exists():
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class PrivatePollRequestView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pas):
        if (PrivatePoll.objects.filter(password=pas)).exists():
            serializer_data = PrivatePoll.objects.filter(password=pas)
            serializer = PrivatePollSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublicPollCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollResult.objects.filter(publicpoll=pk)).exists():
            serializer_data = PublicPollResult.objects.filter(publicpoll=pk)
            serializer = PublicPollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublicPollOptionCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollResult.objects.filter(publicpoll_option=pk)).exists():
            serializer_data = PublicPollResult.objects.filter(publicpoll_option=pk)
            serializer = PublicPollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PrivatePollCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollResult.objects.filter(privatepoll=pk)).exists():
            serializer_data = PrivatePollResult.objects.filter(privatepoll=pk)
            serializer = PrivatePollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PrivatePollOptionCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollResult.objects.filter(privatepoll_option=pk)).exists():
            serializer_data = PrivatePollResult.objects.filter(privatepoll_option=pk)
            serializer = PrivatePollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PersonalPublicPollResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollResult.objects.filter(publicpoll=pk)).exists():
            serializer_data = PublicPollResult.objects.filter(publicpoll=pk)
            serializer = PublicPollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PersonalPrivatePollResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollResult.objects.filter(privatepoll=pk)).exists():
            serializer_data = PrivatePollResult.objects.filter(privatepoll=pk)
            serializer = PrivatePollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SinglePublicPollOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollOption.objects.filter(pk=pk)).exists():
            serializer_data = PublicPollOption.objects.filter(pk=pk)
            serializer = PublicPollOptionSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SinglePrivatePollOptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollOption.objects.filter(pk=pk)).exists():
            serializer_data = PrivatePollOption.objects.filter(pk=pk)
            serializer = PrivatePollOptionSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (UserProfile.objects.filter(pk=pk)).exists():
            serializer_data = UserProfile.objects.filter(pk=pk)
            serializer = UserProfileSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PublicPollResultByUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PublicPollResult.objects.filter(user_profile=pk)).exists():
            serializer_data = PublicPollResult.objects.filter(user_profile=pk)
            serializer = PublicPollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PrivatePollResultByUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        if (PrivatePollResult.objects.filter(user_profile=pk)).exists():
            serializer_data = PrivatePollResult.objects.filter(user_profile=pk)
            serializer = PrivatePollResultSerializer(serializer_data, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)