from rest_framework import serializers
from .models import RewardHistory

class RewardHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardHistory
        fields = ('id', 'created_at', 'current_balance', 'added_balance')
        read_only_fields = ('id', 'created_at', 'current_balance')

    def validate(self, data):
        # Проверяем, что added_balance положительный
        if data['added_balance'] < 0:
            raise serializers.ValidationError("added_balance должен быть положительным числом.")
        return data

    def create(self, validated_data):
        last_record = RewardHistory.objects.last()
        if last_record:
            current_balance = last_record.current_balance + validated_data['added_balance']
        else:
            current_balance = validated_data['added_balance']
        reward_history = RewardHistory.objects.create(
        current_balance=current_balance,
        added_balance=validated_data['added_balance']
    )
        return reward_history