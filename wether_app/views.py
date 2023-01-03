from django.shortcuts import render
import requests
from datetime import datetime


def home(request):
    try:
        city = request.GET.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=41f994fcf86ad8384cf903f481284dca"
        data = requests.get(url).json()
        
        weather = {
            'city' : data['name'], 
            'weather' : data['weather'][0]['main'],
            'description' : data['weather'][0]['description'],  
            'temperature' : int(data['main']['temp'] -273),
            'pressure' : data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'now' : datetime.now()
            }
        return render(request, "home.html",  {'weather' : weather, 'data' : data})
    except KeyError:
        return render(request, "home.html")
    except Exception as e:
        return render(request, "home.html")
