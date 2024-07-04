#from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class HelloView(APIView):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Guest')
        client_ip = request.META.get('REMOTE_ADDR')
        location = 'Unknown'
        temperature = 'Unknown'

        try:
            geo_res = requests.get(f'http://ip-api.com/json/{client_ip}').json()
            location = geo_res['city']
            weather_res = requests.get(f'http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={location}').json()
            temperature = weather_res['current']['temp_c']
        except Exception as e:
            print(e)

        return Response({
            'client_ip': client_ip,
            'location': location,
            'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}'
        })
