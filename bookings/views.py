from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import render
from .models import Booking


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# def booking_list(request):
#     bookings = Booking.objects.all()
#     return render(request, 'bookings/booking_list.html', {'bookings': bookings})
