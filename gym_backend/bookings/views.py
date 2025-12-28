
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from classes.models import Session as GymSession

# Create your views here.

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.select_related("member", "session", "session__course")
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        member_id = request.data.get("member")
        session_id = request.data.get("session")

        if not member_id or not session_id:
            return Response(
                {"detail": "member and session are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # رزرو تکراری
        if Booking.objects.filter(member_id=member_id, session_id=session_id).exists():
            return Response(
                {"detail": "You have already booked this session."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # کنترل ظرفیت
        try:
            gym_session = GymSession.objects.select_related("course").get(id=session_id)
        except GymSession.DoesNotExist:
            return Response(
                {"detail": "Session not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        current_bookings = Booking.objects.filter(session=gym_session).count()
        if current_bookings >= gym_session.course.capacity:
            return Response(
                {"detail": "Session is full."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)
