
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Payment
from .serializers import WalletSerializer, PaymentSerializer

# Create your views here.


class WalletViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Wallet.objects.select_related("member")
    serializer_class = WalletSerializer


class PaymentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.select_related("member")
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        # اگر پرداخت موفق بود، کیف پول را شارژ کن
        if payment.status == Payment.PaymentStatus.SUCCESS:
            wallet, _ = Wallet.objects.get_or_create(member=payment.member)
            wallet.balance += payment.amount
            wallet.save()
