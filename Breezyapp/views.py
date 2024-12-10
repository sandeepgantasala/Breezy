import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime

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

    # Get today's date to exclude it from the forecast
    today = datetime.now().date()

    # Process forecast data: Group by date and select one forecast (closest to midday)
    daily_forecasts = {}
    for forecast in forecast_data.get('list', []):
        date_str = forecast['dt_txt'].split(' ')[0]  # Extract date (YYYY-MM-DD)
        time_str = forecast['dt_txt'].split(' ')[1]  # Extract time (HH:MM:SS)
        forecast_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        if forecast_date > today:  # Exclude today's date
            if date_str not in daily_forecasts or time_str == '12:00:00':  # Closest to midday
                daily_forecasts[date_str] = {
                    'datetime': forecast['dt_txt'],
                    'date': forecast_date,
                    'temperature': forecast['main']['temp'],
                    'description': forecast['weather'][0]['description'].capitalize(),
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
            'description': current_weather_data.get('weather', [{}])[0].get('description', 'N/A').capitalize(),
            'icon': current_weather_data.get('weather', [{}])[0].get('icon', 'N/A'),
        },
        'forecast_list': forecast_list,
    }

    return render(request, 'current_weather.html', context)
