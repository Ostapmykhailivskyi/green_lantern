from django.db import models
from django.db.models import Index
from django.utils.translation import gettext_lazy as _
from apps.orders.managers import OrderQuerySet, OrderManager


class Order(models.Model):
    STATUS_PROCESSED = 'processed'
    STATUS_PENDING_PAYMENT = 'pend_pay'
    STATUS_PAID = 'paid'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PROCESSED, "Processed"),
        (STATUS_PENDING_PAYMENT, "Pending payment"),
        (STATUS_PAID, "Paid"),
        (STATUS_ARCHIVED, "Archived"),
    )

    object = OrderManager.from_queryset(OrderQuerySet)()
    first_name = models.CharField(max_length=32, unique=True)
    last_name = models.CharField(max_length=32, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    message = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=STATUS_PROCESSED, blank=True)
    car = models.ManyToManyField(to='cars.Car', on_delete=models.SET_NULL, null=True, related_name='orders')

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        indexes = [Index(fields=['last_name', 'email'])]

    def __str__(self):
        return f'{self.status.upper()} - {self.car}'
