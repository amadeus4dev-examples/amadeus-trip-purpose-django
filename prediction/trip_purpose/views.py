from amadeus import Client, ResponseError
from django.contrib import messages
from django.shortcuts import render

amadeus = Client()


def prediction(request):
    kwargs = {'originLocationCode': request.POST.get('Origin'),
              'destinationLocationCode': request.POST.get('Destination'),
              'departureDate': request.POST.get('Departuredate'),
              'returnDate': request.POST.get('Returndate')}
    try:
        purpose = amadeus.travel.predictions.trip_purpose.get(
            **kwargs).data['result']

    except ResponseError as error:
        print(error)
        messages.add_message(request, messages.ERROR, error)
        return render(request, 'trip_purpose/home.html', {})
    return render(request, 'trip_purpose/home.html', {'res': purpose})

