from rest_framework import serializers
from budget.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["transaction_type", "transaction_name", "transaction_amount"]


class GroupedSerializer(serializers.Serializer):
    transaction_name = serializers.CharField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
