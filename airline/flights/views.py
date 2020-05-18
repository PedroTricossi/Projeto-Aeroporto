from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Flights, Passengers

# Create your views here.
def index(request):
    context = {
        "flights": Flights.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flights.objects.get(pk=flight_id)
    except Flights.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passengers.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)
    

def passenger(request, passenger_id):
    passenger = Passengers.objects.get(pk=passenger_id)

    context = {
        "passengers": passenger
    }

    return render(request, "flights/passanger.html", context)


def book(request, flight_id):
    try:
        passenger_id = request.POST["passenger"]
        flight = Flights.objects.get(pk=flight_id)
        passenger = Passengers.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selection."})
    except Flights.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passengers.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger."})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

