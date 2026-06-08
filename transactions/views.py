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
from .serializers import (
    TransferSerializer,
    TransactionSerializer
)



from rest_framework import generics
from django.db.models import Q



from django.db.models import Sum


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
    




class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_account = Account.objects.get(user=self.request.user)

        return Transaction.objects.filter(
            Q(from_account=user_account) |
            Q(to_account=user_account)
        ).order_by('-created_at')
    



class DashboardStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        account = Account.objects.get(user=request.user)

        total_sent = Transaction.objects.filter(
            from_account=account
        ).aggregate(
            total=Sum('amount')
        )['total'] or 0

        total_received = Transaction.objects.filter(
            to_account=account
        ).aggregate(
            total=Sum('amount')
        )['total'] or 0

        transaction_count = Transaction.objects.filter(
            Q(from_account=account) |
            Q(to_account=account)
        ).count()

        return Response({
            "balance": account.balance,
            "total_sent": total_sent,
            "total_received": total_received,
            "transaction_count": transaction_count
        })