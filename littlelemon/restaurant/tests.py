from django.test import TestCase
from restaurant.models import Booking
import datetime

# Create your tests here.
class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name='John', reservation_date='2024-03-20')
        Booking.objects.create(first_name='Jane', reservation_date='2024-03-24')

    def test_booking_date(self):
        """The booking by John should be on 2024-03-20."""
        booking_date = datetime.date(2024, 3, 20)
        customer = Booking.objects.filter(first_name='John')
        self.assertEqual(customer.first().reservation_date, booking_date, 'fail message')

    def test_booking_count(self):
        """Two bookings by John and Jane should be added."""
        # self.createBooking()
        customers = Booking.objects.all()
        self.assertEqual(customers.count(), 2, 'fail message')
