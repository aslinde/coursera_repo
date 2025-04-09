from django.test import TestCase
from .models import Reservation
from datetime import datetime
# Create your tests here.

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            first_name = 'John', ## Adding test data in the model
            last_name = 'McDonald'
        )
    def test_fields(self):

        self.assertIsInstance(self.reservation.first_name, str)

        self.assertIsInstance(self.reservation.last_name, str)
        ### if you change it to int the test fails
    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)