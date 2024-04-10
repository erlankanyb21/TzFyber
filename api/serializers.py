from rest_framework import serializers
from .models import RewardHistory

class RewardHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardHistory
        fields = ['id', 'created_at', 'current_balance', 'sid', 'uid', 'amount', 'currency_name', 'currency_id']
        read_only_fields = ('id', 'created_at', 'current_balance')

    def validate(self, data):
        # Проверяем, что amount положительный
        if data['amount'] < 0:
            raise serializers.ValidationError("amount должен быть положительным числом.")
        return data

    def create(self, validated_data):
        # Получаем последнюю запись и ее баланс
        last_record = RewardHistory.objects.last()
        if last_record:
            current_balance = last_record.current_balance
        else:
            current_balance = 0
        
        # Добавляем к текущему балансу значение amount
        current_balance += validated_data['amount']
        
        # Создаем новую запись в истории наград
        reward_history = RewardHistory.objects.create(
            current_balance=current_balance,
            sid=validated_data['sid'],
            uid=validated_data['uid'],
            amount=validated_data['amount'],
            currency_name=validated_data['currency_name'],
            currency_id=validated_data['currency_id']
        )
        return reward_history
