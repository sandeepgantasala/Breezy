import requests
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response 





def current_weather(request):
    city = request.GET.get('city', 'New York')  # Default to New York
    api_key = 'a424055e1768cbb64f5f85adb148cf5e'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    

    context = {
        'city': city,
        'temperature': weather_data.get('main', {}).get('temp', 'N/A'),
        'description': weather_data.get('weather', [{}])[0].get('description', 'N/A'),
    }
    return render(request, 'current_weather.html', context)


def forecast(request):
    city = request.GET.get('city', 'New York')
    api_key = 'a424055e1768cbb64f5f85adb148cf5e'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    forecast_data = response.json()
   

    if response.status_code == 200 and 'list' in forecast_data:
        forecast_list = []
        for forecast in forecast_data['list'][:5]:
            forecast_list.append({
                'datetime': forecast['dt_txt'],
                'temperature': forecast['main']['temp'],
                'description': forecast['weather'][0]['description'],
                'icon': forecast['weather'][0]['icon'],
            })

        context = {
            'city': city,
            'forecast_list': forecast_list,
        }
    else:
        context = {
            'city': city,
            'error': forecast_data.get('message', 'Unable to fetch forecast data.'),
        }

    return render(request, 'forecast.html', context)
