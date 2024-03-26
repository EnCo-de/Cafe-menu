from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10) # time
    number_of_guests = models.IntegerField(default=1) # seat_count
    comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self): 
        return self.first_name

    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=255) 
    slug = models.SlugField() 


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, db_index=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True) 
    menu_item_description = models.TextField(max_length=1000, default='') 
    featured = models.BooleanField(db_index=True)

    def __str__(self):
        return self.name