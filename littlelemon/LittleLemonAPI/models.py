from django.db import models
from django.contrib.auth.models import User
from restaurant.models import MenuItem

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    price = models.DecimalField(max_digits=6, decimal_places=2) 

    class Meta:
        unique_together = ('menuitem', 'user')
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2) 
    date = models.DateField(db_index=True) 


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) 
    price = models.DecimalField(max_digits=6, decimal_places=2) 

    class Meta:
        unique_together = ('order', 'menuitem')