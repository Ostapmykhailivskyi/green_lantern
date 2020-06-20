from django.contrib import admin
from apps.dealers.models import Dealer, City, Country
from django.utils.safestring import mark_safe


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
