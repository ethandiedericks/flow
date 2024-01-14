from rest_framework import serializers


class GroupedSerializer(serializers.Serializer):
    transaction_name = serializers.CharField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
