from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=50, inventory=100)
        self.assertEqual(item.__str__(), 'IceCream')

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name='Test', no_of_guests=5)
        self.assertEqual(item.__str__(), 'Test')


