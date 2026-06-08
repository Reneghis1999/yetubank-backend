from django.shortcuts import render

# Create your views here.
from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.models import Account
from users.models import User
from .models import Transaction
from .serializers import TransferSerializer


class TransferView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransferSerializer(data=request.data)

        if serializer.is_valid():
            receiver_email = serializer.validated_data['receiver_email']
            amount = serializer.validated_data['amount']

            sender_account = Account.objects.get(user=request.user)

            try:
                receiver_user = User.objects.get(email=receiver_email)
                receiver_account = Account.objects.get(user=receiver_user)

            except User.DoesNotExist:
                return Response(
                    {"error": "Receiver not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            if sender_account.balance < amount:
                return Response(
                    {"error": "Insufficient balance"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            sender_account.balance -= amount
            receiver_account.balance += amount

            sender_account.save()
            receiver_account.save()

            Transaction.objects.create(
                from_account=sender_account,
                to_account=receiver_account,
                amount=amount,
                transaction_type='transfer'
            )

            return Response({
                "message": "Transfer successful"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )