from django.db import models
from django.db.models import Index


class Order:
    OrderID = models.AutoField(primary_key=True)
    models.ManyToManyField(to='cars.Car', related_name='orders')
    Status = models.CharField(max_length=10)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(max_length=40, blank=True)
    Phone = models.CharField(max_length=14, default=+000-000-000-000)

    class Meta:
        verbose_name = ('Order',)
        verbose_name_plural = ('Orders',)
        indexes = [
            Index(fields=['last_name', 'email'])
        ]

    @property
    def full_name(self):
        return f'{self.FirstName} {self.LastName}'
