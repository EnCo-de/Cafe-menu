from django.forms import ModelForm
from .models import Booking, MenuItem

# Code for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"