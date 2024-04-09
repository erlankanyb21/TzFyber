from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .models import RewardHistory
from .serializers import RewardHistorySerializer
from rest_framework.views import APIView

# Create your views here.
class RewardHistoryView(APIView):
    reward_serializer = RewardHistorySerializer

    def get_queryset(self):
        return RewardHistory.objects.order_by('-created_at')
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.reward_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.reward_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
