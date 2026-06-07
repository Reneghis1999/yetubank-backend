from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Account
        fields = [
            'username',
            'email',
            'balance',
            'currency'
        ]