import requests
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response 
from django.conf import settings

def current_weather(request):
    city = request.GET.get('city', 'New York')  # Default city
    unit = request.GET.get('unit', 'imperial')  # Default unit (Fahrenheit)
    api_key = settings.OPENWEATHER_API_KEY
    unit_symbol = '°F' if unit == 'imperial' else '°C'

    # Fetch current weather
    current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}'
    current_weather_response = requests.get(current_weather_url)
    current_weather_data = current_weather_response.json()

    # Fetch 5-day forecast
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={unit}'
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    # Process forecast data: Group by date and select one forecast (closest to midday)
    daily_forecasts = {}
    for forecast in forecast_data['list']:
        date = forecast['dt_txt'].split(' ')[0]  # Extract date (YYYY-MM-DD)
        time = forecast['dt_txt'].split(' ')[1]  # Extract time (HH:MM:SS)
        if date not in daily_forecasts or time == '12:00:00':
            daily_forecasts[date] = {
                'datetime': forecast['dt_txt'],
                'temperature': forecast['main']['temp'],
                'description': forecast['weather'][0]['description'],
                'icon': forecast['weather'][0]['icon'],
            }
        if len(daily_forecasts) == 5:  # Limit to 5 unique days
            break

    forecast_list = list(daily_forecasts.values())

    context = {
        'city': city,
        'unit': unit,
        'unit_symbol': unit_symbol,
        'current_weather': {
            'temperature': current_weather_data.get('main', {}).get('temp', 'N/A'),
            'description': current_weather_data.get('weather', [{}])[0].get('description', 'N/A').upper(),
            'icon': current_weather_data.get('weather', [{}])[0].get('icon', 'N/A'),
        },
        'forecast_list': forecast_list,
    }

    return render(request, 'current_weather.html', context)
