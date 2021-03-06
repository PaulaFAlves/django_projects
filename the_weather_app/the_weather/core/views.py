import requests
from django.shortcuts import render
from .models import City

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7bfefe1c10bc028938063a544f8f2254'
	# city = 'Canoas'
	city = request.GET.get('city', 'canoas')
	city = city.title()

	r = requests.get(url.format(city)).json()



	city_weather = {
		'city': city,
		'temperature': r['main']['temp'],
		'description': r['weather'][0]['description'],
		'icon': r['weather'][0]['icon'],
	}



	context = {'city_weather': city_weather}

	return render(request, 'weather/weather.html', context)
