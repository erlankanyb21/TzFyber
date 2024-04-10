from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .models import RewardHistory
from .serializers import RewardHistorySerializer
from rest_framework.views import APIView

# Create your views here.
class RewardHistoryListView(APIView):
    reward_serializer = RewardHistorySerializer

    def get_queryset(self):
        return RewardHistory.objects.order_by('-created_at')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.reward_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class RewardHistoryCreateView(APIView):
    reward_serializer = RewardHistorySerializer

    def get(self, request, *args, **kwargs):
        # Получаем параметры запроса
        data = request.GET
        # Создаем сериализатор с переданными параметрами
        serializer = self.reward_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)