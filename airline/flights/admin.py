from django.contrib import admin

from .models import Airport, Flights, Passengers

# Register your models here.

class PassengerInline(admin.StackedInline):
    model = Passengers.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flights, FlightAdmin)
admin.site.register(Passengers, PassengerAdmin)
