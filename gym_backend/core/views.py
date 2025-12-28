from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import models
from bookings.models import Booking
from finance.models import Wallet, Payment
from classes.models import Session
from rest_framework.permissions import IsAdminUser
from members.models import Member
from classes.models import Course, Session


# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from bookings.models import Booking
from finance.models import Wallet


class MemberDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        member_id = request.query_params.get("member_id", 1)
        total_bookings = Booking.objects.filter(member_id=member_id).count()
        wallet = Wallet.objects.filter(member_id=member_id).first()

        return Response({
            "total_bookings": total_bookings,
            "wallet_balance": wallet.balance if wallet else 0,
            "recent_payments": [],
            "upcoming_sessions": []
        })


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        members_count = Member.objects.count()
        courses_count = Course.objects.count()
        sessions_count = Session.objects.count()
        bookings_count = Booking.objects.count()
        total_income = Payment.objects.filter(status="SUCCESS").aggregate(
            total=models.Sum("amount")
        )["total"] or 0

        return Response({
            "members_count": members_count,
            "courses_count": courses_count,
            "sessions_count": sessions_count,
            "bookings_count": bookings_count,
            "total_income": total_income,
        })
