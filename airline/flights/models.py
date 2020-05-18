from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    stop = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="stop", default="1")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - voo de {self.origin} em direção a {self.destination}"

class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    age = models.IntegerField(blank=True)
    sex = models.CharField(blank=True, max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
