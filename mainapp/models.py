from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)
    sales_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.name