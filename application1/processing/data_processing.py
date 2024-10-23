from datetime import datetime
from collections import defaultdict

daily_weather_data = defaultdict(list)

def process_weather_data(weather):
    city = weather['name']
    temp = weather['main']['temp']
    feels_like = weather['main']['feels_like']
    main_condition = weather['weather'][0]['main']
    timestamp = datetime.utcfromtimestamp(weather['dt']).date()
    
    daily_weather_data[timestamp].append({
        'city': city,
        'temp': temp,
        'feels_like': feels_like,
        'condition': main_condition
    })

def calculate_daily_summary():
    daily_summary = {}
    for date, records in daily_weather_data.items():
        avg_temp = sum(record['temp'] for record in records) / len(records)
        max_temp = max(record['temp'] for record in records)
        min_temp = min(record['temp'] for record in records)
        
        # Dominant weather condition
        condition_count = defaultdict(int)
        for record in records:
            condition_count[record['condition']] += 1
        dominant_condition = max(condition_count, key=condition_count.get)

        daily_summary[date] = {
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
    return daily_summary
