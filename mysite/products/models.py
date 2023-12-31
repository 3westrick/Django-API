from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=250)
    des = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def sale_price(self):
            return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
