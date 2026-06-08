from rest_framework import serializers
from .models import Transaction


class TransferSerializer(serializers.Serializer):
    receiver_email = serializers.EmailField()
    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )


class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(
        source='from_account.user.username'
    )

    receiver = serializers.CharField(
        source='to_account.user.username'
    )

    class Meta:
        model = Transaction
        fields = [
            'id',
            'sender',
            'receiver',
            'amount',
            'transaction_type',
            'created_at'
        ]