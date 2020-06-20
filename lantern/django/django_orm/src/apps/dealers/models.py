from django.db import models
from django.contrib.auth.models import User


class Dealer(User):
    DealerID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=64)
    Email = models.EmailField(max_length=60, blank=True)
    Firstname = models.CharField(max_length=24)
    Lastname = models.CharField(max_length=24)
    CityID = models.ForeignKey('dealers.City', on_delete=models.CASCADE)

    @property
    def full_contact(self):
        return '%s %s %s' % (self.Firstname, self.Lastname, self.Email)


class City(models.Model):
    CityID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    CountryID = models.CharField(max_length=30)


class Country(models.Model):
    CountryID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    code = models.IntegerField(blank=True, null=True)